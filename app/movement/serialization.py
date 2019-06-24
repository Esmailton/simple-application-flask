from app import ma
from .model import MovementModel, MovementEmployee, MovementDescription, MovementValue
from marshmallow  import fields, schema

class MovemenModeltSchema(ma.ModelSchema):
    class Meta: 
        model = MovementModel

    type = fields.Bool(required=True)

class MovementDescriptionSchema(ma.ModelSchema):
    class Meta: 
        model = MovementDescription
    
    movement_id = fields.Int(required=True)
    expense_id = fields.Int(required=True)
    service_id = fields.Int(required=True)

    
class MovementEmployeeSchema(ma.ModelSchema):
    class Meta: 
        model = MovementEmployee

    employee_id = fields.Int(required=True)
    movement_id = fields.Int(required=True)

class MovementValueSchema(ma.ModelSchema):
    class Meta: 
        model = MovementValue

    movement_id = fields.Int(required=True)
    value = fields.Decimal(required=True)
