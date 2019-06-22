from app import db
from datetime import datetime


class Expense(db.Model):

    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

class MovementModel(db.Model):

    __tablename__ = 'movement'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Boolean)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class MovementValue(db.Model):
   
    __tablename__ = 'movement_value'

    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    value = db.Column(db.Numeric(20, 2))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class MovementDescription(db.Model):

    __tablename__ = 'movement_description'

    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    expense_id = db.Column(db.Integer, db.ForeignKey('expense.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class MovementEmployee(db.Model):
   
    __tablename__ = 'movement_employee'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
