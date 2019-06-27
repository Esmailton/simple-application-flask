# -*- encoding: utf-8 -*-

from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import MovementModel, MovementEmployeeModel, MovementDescriptionModel, MovementValueModel, ExpenseModel
from app import db
from .serialization import MovementSchema, MovementDescriptionSchema, MovementEmployeeSchema


class Movement(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, args):

        if args:

            # result =  MovementDescriptionModel.query.get(15)
            # value_model_schema = MovementDescriptionSchema()
            # value_model_result = value_model_schema.dump(result)

            result = MovementModel.query.filter(MovementModel.id==18).first()
            value_model_schema = MovementSchema()
            value_model_result = value_model_schema.dump(result)

            # result = MovementEmployeeModel.query.get(17)
            # value_model_schema = MovementEmployeeSchema()
            # value_model_result = value_model_schema.dump(result)

            return jsonify({
                'movement': value_model_result.data
            }), 200

    def post(self):
        ...
        # movement_schema = MovemenModelSchema()
        # movement_value_schema = MovementValueSchema()
        # movement_employee_schema = MovementEmployeeSchema()
        # movement_description_schema = MovementDescriptionSchema()

        # expense = Expense(
        #     description = 'Conta de Energia'
        #     )
        # db.session.add(expense)
        # db.session.flush()

        # payload = request.json
        # movement_payload = {'type' :payload.get('type')}
        # movement, error = movement_schema.load(movement_payload)

        # if error:
        #     return jsonify(error), 401

        # db.session.add(movement)
        # db.session.flush()

        # if movement.id:
        #     movement_value_payload = {
        #         'movement_id': movement.id,
        #         'value' : payload.get('value')
        #         }
        #     movementvalue, error = movement_value_schema.load(movement_value_payload)
        #     if error:
        #         return jsonify(error), 401

        #     db.session.add(movementvalue)
        #     db.session.flush()

        #     movement_employee = {
        #             'employee_id' : payload.get('employee_id'),
        #             'movement_id': movement.id
        #             }
        #     movementemployee, error = movement_employee_schema.load(movement_employee)
        #     if error:
        #         return jsonify(error), 401

        #     db.session.add(movementemployee)
        #     db.session.flush()

        #     movement_description = {
        #         'movement_id' : movement.id,
        #         'expense_id' : payload.get('expense_id'),
        #         'service_id': payload.get('service_id')
        #     }
        #     movementdescription, error = movement_description_schema.load(movement_description)

        #     if error:
        #         return jsonify(error), 401

        #     db.session.add(movementdescription)
        #     db.session.commit()

        #     return jsonify({
        #             'movement': 'Sucesso!'
        #         }), 201

    def put(self):
        pass

    def delete(self):
        pass
