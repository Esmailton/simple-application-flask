from flask import Blueprint

from .authentication import User

user = Blueprint('user', __name__)

user_view = User.as_view('user_view')

user.add_url_rule(
    '/user/', view_func=user_view, methods=['GET', ])

user.add_url_rule(
    '/user/', view_func=user_view, methods=['POST', ])
user.add_url_rule('/user/<args>/', view_func=user_view,
                  methods=['GET', 'PUT', 'DELETE', ])
