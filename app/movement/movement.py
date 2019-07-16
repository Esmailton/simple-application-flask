# -*- encoding: utf-8 -*-

from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import MovementModel, MovementEmployeeModel, MovementDescriptionModel, MovementValueModel
from ..expense.model import ExpenseModel
from ..employee.model import EmployeeModel
from ..services.model import ServiceModel
from app import db
from sqlalchemy.sql import or_
from sqlalchemy import Date, cast
from .serialization import MovementSchema, MovementDescriptionSchema, MovementEmployeeSchema, MovementValueSchema
from datetime import datetime
from ..authentication.utils.decorators import token_required
from ..authentication.model import Permission


class Movement(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    @token_required(Permission.MEDIUM)
    def get(self, args):

        try:
            if args and args.isdigit():

                movement = MovementModel.query.get(args)
                movement_schema = MovementSchema()
                result = movement_schema.dump(movement)

                return jsonify({
                    'movement': result.data
                }), 200

            if args and not args.isdigit():
                start_date = request.args.get('start_date')
                final_date = request.args.get('final_date')
                type = request.args.get('type')
                status = request.args.get('status')

                movement_query = MovementModel.query\
                    .join(MovementEmployeeModel, MovementEmployeeModel.movement_id == MovementModel.id)\
                    .join(MovementDescriptionModel, MovementDescriptionModel.movement_id == MovementModel.id)\
                    .join(EmployeeModel, EmployeeModel.id == MovementEmployeeModel.employee_id)\
                    .outerjoin(ExpenseModel, ExpenseModel.id == MovementDescriptionModel.expense_id)\
                    .outerjoin(ServiceModel, ServiceModel.id == MovementDescriptionModel.service_id)

                if args:
                    movement_query = movement_query.filter(or_(
                        EmployeeModel.name.ilike('%{}%'.format(args)),
                        ExpenseModel.description.ilike('%{}%'.format(args)),
                        ServiceModel.description.ilike('%{}%'.format(args))
                    ))

                if type:
                    movement_query = movement_query.filter(
                        MovementModel.type == type)

                if status:
                    movement_query = movement_query.filter(
                        MovementModel.status == status)

                if start_date and final_date:
                    movement_query = movement_query.filter(
                        cast(MovementModel.create_at, Date).between(start_date, final_date))

                movement_schema = MovementSchema(many=True)
                result = movement_schema.dump(movement_query)
                return jsonify({
                    'movement': result.data
                }), 200

            else:
                movement = MovementModel.query.all()
                movement_schema = MovementSchema(many=True)
                result = movement_schema.dump(movement)

                return jsonify({
                    'movement': result.data
                }), 200

        except:
            return jsonify({
                'error': 'try again bad, request!'
            }), 401

    def post(self):

        if request.json:

            payload = request.json
            movement_schema = MovementSchema()
            movement_payload = {
                'type': payload.get('type'),
                'status': payload.get('status')
            }

            movement, error = movement_schema.load(movement_payload)

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
                    movement_employee
                )

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
                    'movement': movement_payload
                }), 201

        else:
            return jsonify({
                'error': 'try again bad, request!'
            }), 401

    def put(self):
        pass

    def delete(self):
        pass
