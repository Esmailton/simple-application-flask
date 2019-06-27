from app import db
from datetime import datetime

class ServiceModel(db.Model):

    __tablename__ = 'service'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, description):
        self.description = description