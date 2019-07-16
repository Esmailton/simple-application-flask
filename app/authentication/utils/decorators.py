from functools import wraps
import jwt
from flask import request, jsonify, current_app, abort
from ..model import UserModel


def token_required(permission):
    def decorador(f):
        @wraps(f)
        def _verify(*args, **kwargs):
            auth_headers = request.headers.get('Authorization', '').split()

            if len(auth_headers) != 2:
                return jsonify({'Token': 'token_missing'}), 401

            try:
                token = auth_headers[1]
                data = jwt.decode(token, current_app.config['SECRET_KEY'])
                user = UserModel.query.filter(
                    UserModel.id == data['user_id'], UserModel.active == True).first()

                if not user.can(permission):
                    return jsonify({'Permisson': 'permission_denied_msg'}), 403

                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify({'Token': 'token_expired'}), 401
            except (jwt.InvalidTokenError, Exception) as e:
                return jsonify({'Invalid': 'invalid_token'}, msg={"token": data}), 401

        return _verify
    return decorador
