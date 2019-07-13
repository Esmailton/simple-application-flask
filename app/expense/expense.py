# -*- encoding: utf-8 -*-

from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import ExpenseModel
from app import db
from .serialization import ExpenseSchema


class Expense(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, args):
        try:

            if args and args.isdigit():

                expense_schema = ExpenseSchema()
                result = ExpenseModel.query.get(args)
                expense = expense_schema.dump(result)
                return jsonify({'expense': expense.data}), 200

            if args and not args.isdigit():
                expense_schema = ExpenseSchema(many=True)
                result = ExpenseModel.query.filter(
                    ExpenseModel.description.ilike('%{}%'.format(args)))
                expense = expense_schema.dump(result)
                return jsonify({'expense': expense.data}), 200

            else:
                expense_schema = ExpenseSchema(many=True)
                result = ExpenseModel.query.all()
                expenses = expense_schema.dump(result)
                return jsonify({'user': expenses.data}), 200

        except:
            return jsonify({'error': 'Error while fetching data!'}), 404

    def post(self):

        if request.json:

            try:
                expense_schema = ExpenseSchema()
                expense, error = expense_schema.load(request.json)

                if error:
                    return jsonify(error), 401

                else:
                    db.session.add(expense)
                    db.session.commit()
                    expense = expense_schema.dump(expense)

                    return jsonify({
                        'expense': expense.data
                    })

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401

        else:
            return jsonify({
                'error': 'try again bad, request!'
            }), 401

    def put(self, args):

        if request.json and args:
            try:
                expense_schema = ExpenseSchema()
                expense = ExpenseModel.query.filter(
                    ExpenseModel.id == args)
                expense.update(request.json)
                db.session.commit()

                return jsonify({
                    'expense': expense_schema.dump(expense).data
                }), 200

            except:
                db.session.rollback()
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401

    def delete(self, args):

        if args:

            try:
                expense = ExpenseModel.query.filter(
                    ExpenseModel.id == args).first()
                db.session.delete(expense)
                db.session.commit()
                return jsonify({
                    'Ok': 'Delete sucess!'
                }), 200

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401
        else:
            return jsonify({
                'error': 'try again bad, request!'
            }), 401
