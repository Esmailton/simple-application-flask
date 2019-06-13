from app import db
from datetime import datetime


class MovementOut(db.Model):

    __tablename__ = 'movement_out'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


class Movement(db.Model):

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


class MovementEmployee(db.Model):
   
    __tablename__ = 'movement_employee'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    movement_id = db.Column(db.Integer, db.ForeignKey('movement.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)