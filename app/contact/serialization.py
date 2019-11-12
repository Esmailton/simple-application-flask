from app import ma
from .model import ContactModel
from ..employee.serialization import EmployeeSchema
from marshmallow import fields, validates, ValidationError


class ContactSchema(ma.ModelSchema):
    class Meta:
        model = ContactModel
        
    contact = fields.Str(required=True)
    employee_id = fields.Int(allow_none=True, load_only=True)