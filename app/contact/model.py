from app import db
from datetime import datetime


class ContactModel(db.Model):

    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(255))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)