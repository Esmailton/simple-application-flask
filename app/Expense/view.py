from flask import Blueprint

from .expense import Expense

expense = Blueprint('expense', __name__)

expense_view = Expense.as_view('expense_view')

expense.add_url_rule(
    '/expense/', defaults={'args': None}, view_func=expense_view, methods=['GET', ])

expense.add_url_rule(
    '/expense/', view_func=expense_view, methods=['POST', ])
expense.add_url_rule('/expense/<args>/', view_func=expense_view,
                     methods=['GET', 'PUT', 'DELETE', ])
