from app import ma
from .model import EmployeeModel
from marshmallow import fields, ValidationError

class EmployeeSchema(ma.ModelSchema):
    class Meta: 
        model = EmployeeModel

    name = fields.Str(required=True)
