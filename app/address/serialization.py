from app import ma
from .model import AddressModel
from marshmallow import fields, validates, ValidationError


class AddressSchema(ma.ModelSchema):
    
    class Meta:
        model = AddressModel
        
    address = fields.Str(required=True),
    neighborhood = fields.Str(required=True),
    number = fields.Int(required=True),
    cep = fields.Str(required=True),
    uf = fields.Str(required=True),
    city = fields.Str(required=True),  
    employee_id = fields.Int(allow_none=True, load_only=True)
