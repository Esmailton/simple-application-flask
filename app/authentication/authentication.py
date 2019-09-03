from flask import request, abort, request, jsonify, current_app
from flask.views import MethodView
from .model import UserModel
from app import db
import jwt
from .serialization import UserSchema
import datetime
from .utils.decorators import token_required
from .model import Permission


class User(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    @token_required(Permission.LOW)
    def get(self):
        auth_headers = request.headers.get('Authorization', '').split()

        print(auth_headers)

        if len(auth_headers) != 2:
            return jsonify({'Token': 'token_missing'}), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])

            return jsonify({
                'user_name': data['user_name']
            })

            return jsonify({'Permisson': 'permission_denied_msg'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'Token': 'token_expired'}), 401
        except (jwt.InvalidTokenError, Exception) as e:
            return jsonify({'Invalid': 'invalid_token'}, msg={"token": data}), 401

    def post(self):

        if request.json:
            auth_json = request.json

            if auth_json.get('operation_type'):
                operation_type = auth_json.get('operation_type')

                # Login
                if operation_type == 'sign_in':
                    auth_json = request.json
                    if auth_json:
                            
                        user = UserModel.query.filter(UserModel.user_name == auth_json.get(
                            'user_name'), UserModel.active == True)
                        
                        user_schema = UserSchema(many=True)
                        result = user_schema.dump(user)
                        
                        user = user.first()
                        if user and user.verify_password(auth_json.get('password')):
                            payload = {
                                'user_id': user.id,
                                'user_name': user.user_name,
                                'role': user.role_id,
                                'iat': datetime.datetime.utcnow(),
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
                            }

                            token = jwt.encode(
                                payload, current_app.config['SECRET_KEY'], current_app.config['JWT_ALGORITHM'])


                        return jsonify(
                            {
                                'token': token.decode('UTF-8'),
                                'user': {
                                    'user': result.data
                                }
                            })

                        # else:
                        #     return jsonify({'Incorect': 'user_or_password_incorrect'}), 401

                    else:
                        return jsonify({'Incorect': 'user_or_password_incorrect'}), 401

                # Casatro
                if operation_type == 'sign_up':
                    user_schema = UserSchema()
                    user, error = user_schema.load(request.json)

                    if error:
                        if error:
                            return jsonify(error), 401

                    try:
                        if user:
                            db.session.add(user)
                            db.session.commit()
                            user = user_schema.dump(user)

                            return jsonify({
                                'user': 'ok'
                            }), 201

                        else:
                            return jsonify({
                                'error': 'try again bad, request!'
                            }), 401

                    except:
                        return jsonify({
                            'error': 'try again bad, request!'
                        }), 401
                else:
                    return jsonify({
                        'error': 'try again bad, request!'
                    }), 401

    def put(self):
        ...
