import datetime
from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import EmployeeModel
from ..address.model import AddressModel
from app import db
from .serialization import EmployeeSchema
from ..address.serialization import AddressSchema
from ..authentication.utils.decorators import token_required
from ..authentication.model import Permission


class Employee(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)

    @token_required(Permission.LOW)
    def get(self, employee_id):

        try:

            if employee_id and employee_id.isdigit():
                employee_schema = EmployeeSchema()
                result = EmployeeModel.query.get(employee_id)
                employee = employee_schema.dump(result)
                return jsonify({'employee': employee.data}), 200

            if employee_id and not employee_id.isdigit():
                employee_schema = EmployeeSchema(many=True)
                result = EmployeeModel.query.filter(
                    EmployeeModel.name.ilike('%{}%'.format(employee_id)))
                employee = employee_schema.dump(result)
                return jsonify({'employee': employee.data}), 200

            else:

                employee_schema = EmployeeSchema(many=True)
                result = EmployeeModel.query.all()
                employees = employee_schema.dump(result)
                return jsonify({'user': employees.data}), 200

        except:
            return jsonify({'error': 'Error while fetching data!'}), 404

    @token_required(Permission.LOW)
    def post(self):
        
        if request:
            
            payload = request.json
            if payload:
                try:
                    employee_schema = EmployeeSchema()

                    payload_employee = {
                        'name': payload.get('name'),
                        'cpf': payload.get('cpf'),
                        'birth_date': payload.get('birth_date')
                    }
                   
                    employee, error = employee_schema.load(payload_employee)

                    if error:
                        return jsonify(error)
                    
                    db.session.add(employee)
                    db.session.flush()
                        
                    if employee.id:
                                                
                        address_schema = AddressSchema()
                        address_payload = {
                            'address': payload.get('address'),
                            'neighborhood': payload.get('neighborhood'),
                            'number': payload.get('number'),
                            'cep': payload.get('cep'),
                            'uf': payload.get('uf'),
                            'city': payload.get('city'),  
                            'employee_id': employee.id            
                        }
                        
                        address, error = address_schema.load(address_payload)
                            
                        if error:
                            return jsonify(error), 400

                        db.session.add(address)
                        db.session.flush()
                        
                    employee = employee_schema.dump(employee)
                    
                    db.session.commit()
                    return jsonify({
                        'employee':' employee.data'
                    }), 201

                except Exception as e:
                    return jsonify({'error': '{} bad request, review data and try again!'.format(e)})
                
            else:
               return jsonify({'error': 'bad request, review data and try again!'}), 404

        else:
            return jsonify({'error': 'bad request, review data and try again!'}), 404

    @token_required(Permission.LOW)
    def put(self, employee_id):

        if employee_id:

            try:
                employee_schema = EmployeeSchema()
                employee = EmployeeModel.query.filter(
                    EmployeeModel.id == employee_id)
                employee.update(request.json)
                db.session.commit()
                return employee_schema.jsonify(employee.first())

            except:
                return jsonify({'error': 'bad request, review data and try again!'}), 404
        else:
            return jsonify({'error': 'bad request, review data and try again!'}), 404

    @token_required(Permission.ADMIN)
    def delete(self, employee_id):

        if employee_id:
            try:
                employee = EmployeeModel.query.filter(
                    EmployeeModel.id == employee_id).first()
                db.session.delete(employee)
                db.session.commit()
                return jsonify({'OK': 'sucess'})
            except:
                return jsonify({'error': 'bad request, review data and try again!'}), 404
        else:
            return jsonify({'error': 'bad request, review data and try again!'}), 404
