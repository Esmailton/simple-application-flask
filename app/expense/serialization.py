from app import ma
from .model import ExpenseModel
from marshmallow import fields, validates, ValidationError


class ExpenseSchema(ma.ModelSchema):
    class Meta:
        model = ExpenseModel

        description = fields.Str(required=True)
