from flask import Blueprint

from .authentication import User

user = Blueprint('user', __name__)

user_view = User.as_view('user_view')

user.add_url_rule(
    '/user/', defaults={'user_id': None}, view_func=user_view, methods=['GET', ])

user.add_url_rule(
    '/user/', view_func=user_view, methods=['POST', ])
user.add_url_rule('/user/<user_id>/', view_func=user_view,
                  methods=['GET', 'PUT', 'DELETE', ])
