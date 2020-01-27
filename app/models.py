from app import db
from datetime import datetime


class Receipt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    usage_id = db.Column(db.Integer, db.ForeignKey('usage.id'))

    def __repr__(self):
        return '<Receipt {}>'.format(self.amount)


class Usage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    receipts = db.relationship('Receipt', backref='use', lazy="dynamic")

    def __repr__(self):
        return '<Usage {}>'.format(self.name)