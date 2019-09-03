from app import ma
from .model import UserModel, Role
from ..employee.serialization import EmployeeSchema
from marshmallow import fields, validates, ValidationError


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel

    user_name = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    password_hash = fields.Str(allow_none=True, load_only=True)
    avata = fields.Str(allow_none=True, load_only=True)
    role_id = fields.Int(allow_none=True, load_only=True)
    active = fields.Bool(required=True)
    employee_id = fields.Int(allow_none=True, load_only=True)
    employee = fields.Nested(EmployeeSchema, only=['name'])
    role = fields.Nested('RoleSchema', only=['name'])
    

class RoleSchema(ma.ModelSchema):
    class Meta:
        model = Role

        name = fields.Str(required=True)
