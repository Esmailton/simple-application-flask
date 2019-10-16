from app import db
from datetime import datetime

class AddressModel(db.Model):

    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    neighborhood = db.Column(db.String(255))
    number = db.Column(db.Integer)
    cep = db.Column(db.String(255))
    city = db.Column(db.String(255))
    uf = db.Column(db.String(255))
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
