from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import UserModel
from app import db
from .serialization import UserSchema


class User(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, args):
        ...

    def post():

        if request.json:
            user_schema = UserSchema()
            user, error, user_schema.load(request.json)

            if error:
                if error:
                    return jsonify(error), 401

            try:
                if user:
                    db.session.add(user)
                    db.session.commit()
                    user = user_schema.dump(user)

                    return jsonify({
                        'user': user.data
                    }), 201

                else:
                    return jsonify({
                        'error': 'try again bad, request!'
                    }), 401

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401

    def put():
        ...
