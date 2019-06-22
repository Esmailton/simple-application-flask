# -*- encoding: utf-8 -*-

from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import MovementModel, MovementEmployee, MovementDescription, MovementValue, Expense
from app import db
from .serialization import MovemenModeltSchema, MovementValueSchema, MovementEmployeeSchema, MovementDescriptionSchema


class Movement(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, args):
        
        if args:

            result = MovementModel.query.join(MovementValue, MovementValue.movement_id==MovementModel.id)\
                .join(MovementDescription, MovementModel.id==MovementDescription.movement_id)\
                .join(MovementEmployee, MovementEmployee.movement_id==MovementModel.id).all()

            print(result)

            return jsonify({
                'movement': 'Sucesso!'
            }), 201
        

    def post(self):
        movement_schema = MovemenModeltSchema()
        Movementvalue_schema = MovementValueSchema()
        Movementemployee_schema = MovementEmployeeSchema()
        Movementdescription_schema = MovementDescriptionSchema()
        


        expense = Expense(
            description = 'Conta de Energia'
            )
        db.session.add(expense)
        db.session.flush()
    
        payload = request.json
        movement_payload = {'type' :payload.get('type')}
        movement, error = movement_schema.load(movement_payload)

        if error:
            return jsonify(error), 401

        db.session.add(movement)
        db.session.flush()

        if movement.id:
            movement_value_payload = {
                'movement_id': movement.id,
                'value' : payload.get('value')
                }
            movementvalue, error = Movementvalue_schema.load(movement_value_payload)
            if error:
                return jsonify(error), 401

            db.session.add(movementvalue)
            db.session.flush()

            movement_employee = {
                    'employee_id' : payload.get('employee_id'),
                    'movement': movement.id
                    }
            movementemployee, error = Movementemployee_schema.load(movement_employee)
            if error:
                return jsonify(error), 401

            db.session.add(movementemployee)
            db.session.flush()
        
            movement_description = {
                'movement_id' : movement.id,
                'expense_id' : payload.get('expense_id'),
                'service_id': payload.get('service_id')
            }
            movementdescription, error = Movementemployee_schema.load(movement_description)

            print(movementdescription)
            if error:
                return jsonify(error), 401

            db.session.add(movementdescription)
            db.session.commit()

            return jsonify({
                    'movement': 'Sucesso!'
                }), 201


    def put(self):
        pass

    def delete(self):
        pass