from app import ma
from .model import EmployeeModel
from ..address.serialization import AddressSchema
from ..contact.serialization import ContactSchema
from marshmallow import fields, ValidationError

class EmployeeSchema(ma.ModelSchema):
    
    class Meta: 
        model = EmployeeModel
        
    name = fields.Str(required=True)
    cpf = fields.Str(required=True)
    birth_date = fields.Str(required=True)
    
    address = fields.Nested(
        'AddressSchema', many=True
    )
    
    contact = fields.Nested(
        'ContactSchema', many=True
    )
