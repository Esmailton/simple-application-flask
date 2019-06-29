# -*- encoding: utf-8 -*-

from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import MovementModel, MovementEmployeeModel, MovementDescriptionModel, MovementValueModel
from app import db
from .serialization import MovementSchema, MovementDescriptionSchema, MovementEmployeeSchema, MovementValueSchema


class Movement(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, args):

        if args:

            movement = MovementModel.query.get(args)
            movement_schema = MovementSchema()
            result = movement_schema.dump(movement)

            return jsonify({
                'movement': result.data
            }), 200

    def post(self):

        if request.json:

            payload = request.json
            print(payload)
            movement_schema = MovementSchema()
            movement_payload = {'type': payload.get('type')}
            print(movement_payload)
            movement, error = movement_schema.load(movement_payload)
            print(error, movement)
            if error:
                return jsonify(error), 401

            db.session.add(movement)
            db.session.flush()

            if movement.id:
                movement_value_schema = MovementValueSchema()
                movement_value_payload = {
                    'movement_id': movement.id,
                    'value': payload.get('value')
                }
                movementvalue, error = movement_value_schema.load(
                    movement_value_payload)

                if error:
                    return jsonify(error), 401

                db.session.add(movementvalue)
                db.session.flush()

                movement_employee_schema = MovementEmployeeSchema()
                movement_employee = {
                    'employee_id': payload.get('employee_id'),
                    'movement_id': movement.id
                }
                movementemployee, error = movement_employee_schema.load(
                    movement_employee)

                if error:
                    return jsonify(error), 401

                db.session.add(movementemployee)
                db.session.flush()

                movement_description_schema = MovementDescriptionSchema()
                movement_description = {
                    'movement_id': movement.id,
                    'expense_id': payload.get('expense_id'),
                    'service_id': payload.get('service_id')
                }
                movementdescription, error = movement_description_schema.load(
                    movement_description)

                if error:
                    return jsonify(error), 401

                db.session.add(movementdescription)
                db.session.commit()

                return jsonify({
                    'movement': 'Sucesso!'
                }), 201

        else:
            return jsonify({
                'error': 'Error'
            }), 400

    def put(self):
        pass

    def delete(self):
        pass
