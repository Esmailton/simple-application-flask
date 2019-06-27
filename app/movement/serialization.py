from app import ma
from .model import MovementModel, MovementEmployeeModel, MovementDescriptionModel, MovementValueModel
from marshmallow import fields
from app.services.serialization import ServiceSchema
from app.employee.serialization import EmployeeSchema


class MovementSchema(ma.ModelSchema):
    class meta:
        Model = MovementModel

    type = fields.Bool(required=True)
    movement_employee = fields.Nested('MovementEmployeeSchema', many=True)
    movement_value = fields.Nested('MovementValueSchema', many=True)
    movement_description = fields.Nested(
        'MovementDescriptionSchema', many=True)


class MovementDescriptionSchema(ma.ModelSchema):
    class meta:
        Model = MovementDescriptionModel
    service = fields.Nested(ServiceSchema, only=['description'])
    movement = fields.Nested(MovementSchema)

    expense_id = fields.Int(required=True)
    service_id = fields.Int(required=True)


class MovementEmployeeSchema(ma.ModelSchema):

    class meta:
        model = MovementEmployeeModel

    employee_id = fields.Int(required=True)
    employee = fields.Nested(EmployeeSchema, only=['name'])


class MovementValueSchema(ma.ModelSchema):
    class meta:
        model = MovementValueModel
    value = fields.Int(required=True)
