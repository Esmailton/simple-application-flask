from app import ma
from .model import MovementModel, MovementEmployeeModel, MovementDescriptionModel, MovementValueModel
from marshmallow import fields
from ..services.serialization import ServiceSchema
from ..employee.serialization import EmployeeSchema
from ..expense.serialization import ExpenseSchema


class MovementSchema(ma.ModelSchema):
    class Meta:
        model = MovementModel

    type = fields.Bool(required=True)
    status = fields.Bool(required=True)

    movement_employee = fields.Nested(
        'MovementEmployeeSchema', only=['employee'], many=True)

    movement_value = fields.Nested(
        'MovementValueSchema', only=['value'], many=True)

    movement_description = fields.Nested(
        'MovementDescriptionSchema', only=['service', 'expense'], many=True)


class MovementDescriptionSchema(ma.ModelSchema):

    class Meta:
        model = MovementDescriptionModel

    service = fields.Nested(ServiceSchema, only=['description'])
    expense = fields.Nested(ExpenseSchema, only=['description'])
    movement = fields.Nested(MovementSchema)

    service_id = fields.Int(allow_none=True)
    expense_id = fields.Int(allow_none=True)

    movement_id = fields.Int(required=True)


class MovementEmployeeSchema(ma.ModelSchema):

    class Meta:
        model = MovementEmployeeModel

    employee_id = fields.Int(required=True)
    employee = fields.Nested(EmployeeSchema, only=['name'])
    movement_id = fields.Int(required=True)


class MovementValueSchema(ma.ModelSchema):
    class Meta:
        model = MovementValueModel

    value = fields.Int(required=True)
    movement_id = fields.Int(required=True)
