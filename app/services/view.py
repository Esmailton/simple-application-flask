from flask import Blueprint

from .service import Service

service = Blueprint('service', __name__)

service_view = Service.as_view('service_view')

service.add_url_rule(
    '/service/', defaults={'service_id': None}, view_func=service_view, methods=['GET', ])

service.add_url_rule(
    '/service/', view_func=service_view, methods=['POST', ])
service.add_url_rule('/service/<service_id>/', view_func=service_view,
                       methods=['GET', 'PUT', 'DELETE', ])
