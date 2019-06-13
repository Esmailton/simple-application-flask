from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import Movement, MovementEmployee, MovementOut, MovementValue
from app import db
from .serialization import MovementSchema, MovementValueSchema, MovementEmployeeSchema



class Employee(MethodView):

    def get(self, args):
        
        if movement_id:
            query = Movement.query.filter(Movement.id == movement_id)
            return query
        else:
            query_all = Movement.query.all()
            return query_all


    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass