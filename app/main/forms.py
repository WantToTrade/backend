from flask.ext.wtf import Form
from wtforms.fields.html5 import (IntegerField,
                                  DateField)
from wtforms import SelectField, FloatField

from ..models import Offer, CURRENCIES

CURRENCIES = [(c, c) for c in CURRENCIES]

class OfferForm(Form):
    currency_from = SelectField('From currency', choices=CURRENCIES)
    currency_to = SelectField('To currency', choices=CURRENCIES)
    amount = IntegerField('Amount')
    expires = DateField('Expiration date')
    latitude = FloatField('Latitude', default=49.22573)
    longitude = FloatField('Longitude', default=16.58205)
