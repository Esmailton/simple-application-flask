from app import db
from datetime import datetime
from ..address.model import AddressModel
from ..contact.model import ContactModel


class EmployeeModel(db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpf = db.Column(db.String(255))
    birth_date = db.Column(db.DateTime)
    address = db.relationship("AddressModel")
    contact = db.relationship("ContactModel")
    create_at = db.Column(db.DateTime, default=datetime.utcnow)