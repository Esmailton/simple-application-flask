from app import db
from datetime import datetime
from ..employee.model import EmployeeModel

class ContactModel(db.Model):

    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(255))
    employee = db.relationship("EmployeeModel")
    create_at = db.Column(db.DateTime, default=datetime.utcnow)