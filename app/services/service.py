from flask import request, abort, request, jsonify
from flask.views import MethodView
from .model import ServiceModel
from app import db
from .serialization import ServiceSchema



class Service(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') and not request.json:
            abort(400)


    def get(self, service_id):

            try:
                if service_id:
                    result = ServiceModel.query.get(service_id)
                    service_schema = ServiceSchema()
                    service = service_schema.dump(result)

                    if service:
                        return jsonify({
                            'service': service.data
                        }), 200

                    else:
                        return jsonify({
                            'Not Fount': 'Not Fount'
                        }), 404

                else:
                    service_schema = ServiceSchema(many=True)
                    result = ServiceModel.query.all()
                    service = service_schema.dump(result)

                    return jsonify({'services': service.data}), 200

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401


    def post(self):

        if request.json:

            service_schema = ServiceSchema()
            service, error = service_schema.load(request.json)

            if error:
                if error:
                 return jsonify(error), 401

            try:
                if service:
                    db.session.add(service)
                    db.session.commit()
                    service = service_schema.dump(service)
                    
                    return jsonify({
                        'service': service.data
                    }), 201

                else:
                    return jsonify({
                    'error': 'try again bad, request!'
                }), 401 

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401

    def put(self, service_id):
                
        if request.json and service_id:
            try:
                service_schema = ServiceSchema()
                service = ServiceModel.query.filter(ServiceModel.id ==service_id)
                service.update(request.json)
                db.session.commit()
                return jsonify({
                    'service': service_schema.dump(service.first()).data
                }), 200

            except:
                return jsonify({
                    'error': 'try again bad, request!'
                }), 401

    def delete(self, service_id):

        if service_id:
            try:
                service = ServiceModel.query.filter( ServiceModel.id==service_id).first()
                db.session.delete(service)
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