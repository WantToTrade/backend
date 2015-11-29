from . import db

CURRENCIES = "CZK", "EUR"

class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    currency_from = db.Column(db.Enum(*CURRENCIES))
    currency_to = db.Column(db.Enum(*CURRENCIES))
    amount = db.Column(db.Integer)
    expires = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
