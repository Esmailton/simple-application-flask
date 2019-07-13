from app import ma
from .model import UserModel
from marshmallow import fields


class UserSchema(ma.ModelSchema):
    class Meta:
        model: UserModel

    user_name = fields.Str(required=True)
    password = fields.Str(required=True)
    active = fields.Bool(required=True)
    role_id = fields.Int(required=True)
