from flask import Blueprint

from .movement import Movement

movement = Blueprint('movement', __name__)

movement_view = Movement.as_view('movement_view')

movement.add_url_rule(
    '/movement/', defaults={'args': None}, view_func=movement_view, methods=['GET', ])

movement.add_url_rule(
    '/movement/', view_func=movement_view, methods=['POST', ])
movement.add_url_rule('/movement/<args>/', view_func=movement_view,
                       methods=['GET', 'PUT', 'DELETE', ])

