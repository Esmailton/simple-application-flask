from app import ma
from .model import MovementModel, MovementEmployee, MovementDescription, MovementValue
from marshmallow import fields, validates, ValidationError

class MovemenModeltSchema(ma.ModelSchema):
    class Meta: 
        model = MovementModel

class MovementDescriptionSchema(ma.ModelSchema):
    class Meta: 
        model = MovementDescription

class MovementEmployeeSchema(ma.ModelSchema):
    class Meta: 
        model = MovementEmployee

class MovementValueSchema(ma.ModelSchema):
    class Meta: 
        model = MovementValue


