from app import db
from datetime import datetime

class EmployeeModel(db.Model):

    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)