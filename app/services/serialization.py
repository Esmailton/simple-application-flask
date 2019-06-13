from app import ma
from .model import ServiceModel
from marshmallow import fields, validates, ValidationError



class ServiceSchema(ma.ModelSchema):
    class Meta:
        model = ServiceModel


        description = fields.Str(required=True)