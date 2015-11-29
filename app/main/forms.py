from flask.ext.wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form

from ..models import Offer

OfferForm = model_form(Offer, base_class=Form)
