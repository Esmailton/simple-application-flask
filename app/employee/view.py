from flask import Blueprint

from .employee import Employee

employee = Blueprint('employee', __name__)

employee_view = Employee.as_view('employee_view')

employee.add_url_rule(
    '/employee/', defaults={'employee_id': None}, view_func=employee_view, methods=['GET', ])

employee.add_url_rule(
    '/employee/', view_func=employee_view, methods=['POST', ])
employee.add_url_rule('/employee/<employee_id>/', view_func=employee_view,
                       methods=['GET', 'PUT', 'DELETE', ])
