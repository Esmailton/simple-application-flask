from app import ma
from .model import Movement, MovementEmployee, MovementOut, MovementValue
from marshmallow import fields, validates, ValidationError

class MovementSchema(ma.ModelSchema):
    class Meta: 
        model = Movement

class MovementOutSchema(ma.ModelSchema):
    class Meta: 
        model = MovementOut

class MovementEmployeeSchema(ma.ModelSchema):
    class Meta: 
        model = MovementEmployee

class MovementValueSchema(ma.ModelSchema):
    class Meta: 
        model = MovementValue


