from app import db
from datetime import datetime
from app.services.model import ServiceModel
from ..employee.model import EmployeeModel


class ExpenseModel(db.Model):

    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class MovementModel(db.Model):

    __tablename__ = 'movement'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Boolean)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    movement_value = db.relationship("MovementValueModel")
    movement_employee = db.relationship("MovementEmployeeModel")
    movement_description = db.relationship("MovementDescriptionModel")


class MovementValueModel(db.Model):

    __tablename__ = 'movement_value'

    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    value = db.Column(db.Numeric(20, 2))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class MovementDescriptionModel(db.Model):

    __tablename__ = 'movement_description'

    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    service = db.relationship("ServiceModel")


class MovementEmployeeModel(db.Model):

    __tablename__ = 'movement_employee'

    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    employee = db.relationship("EmployeeModel")
