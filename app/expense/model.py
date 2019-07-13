from app import db, ma
from datetime import datetime


class ExpenseModel(db.Model):

    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
