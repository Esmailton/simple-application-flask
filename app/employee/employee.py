from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import EmployeeModel
from app import db
from .serialization import EmployeeSchema

class Employee(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, employee_id):

        try:

            if employee_id and employee_id.isdigit(): 
                employee_schema = EmployeeSchema()
                result = EmployeeModel.query.get(employee_id)
                employee = employee_schema.dump(result)
                return jsonify({'employee': employee.data}), 200


            if employee_id and not employee_id.isdigit():
                employee_schema = EmployeeSchema(many=True)
                result = EmployeeModel.query.filter( EmployeeModel.name.ilike('%{}%'.format(employee_id)))
                employee = employee_schema.dump(result)
                return jsonify({'employee': employee.data}), 200

            else:

                employee_schema = EmployeeSchema(many=True)
                result = EmployeeModel.query.all()
                employees = employee_schema.dump(result)
                return jsonify({'user': employees.data}), 200

        except:
            return jsonify({'error': 'Error while fetching data!'}), 404


    def post(self):

        try:
            employee_schema = EmployeeSchema()
            employee, error = employee_schema.load(request.json)
            
            if error:
                return jsonify(error), 401

            db.session.add(employee)
            db.session.commit()
            employee = employee_schema.dump(employee)
    
            return jsonify({
                'employee': employee.data
            }), 201

        except:
            return jsonify({'error': 'bad request, review data and try again!'}), 404

    def put(self, employee_id):

        if employee_id:

            try:
                employee_schema = EmployeeSchema()
                employee = EmployeeModel.query.filter(EmployeeModel.id==employee_id)
                employee.update(request.json)
                db.session.commit()
                return employee_schema.jsonify(employee.first())

            except:
                return jsonify({'error': 'bad request, review data and try again!'}), 404
        else:
            return jsonify({'error': 'bad request, review data and try again!'}), 404


    def delete(self, employee_id):

        if employee_id:
            try:
                employee = EmployeeModel.query.filter(EmployeeModel.id==employee_id).first()
                db.session.delete(employee)
                db.session.commit()
                return jsonify({'OK': 'sucess'})
            except:
                return jsonify({'error': 'bad request, review data and try again!'}), 404
        else:
            return jsonify({'error': 'bad request, review data and try again!'}), 404
