from datetime import datetime

from flask.ext.googlemaps import Map

from flask import render_template, redirect
from . import main
from .forms import OfferForm
from ..models import Offer
from .. import db

@main.route('/')
def index():
    gmap = Map(identifier="view-side",
               lat=49.22573,
               lng=16.58205,
               style="height:600px;width:100%;")
    offers = Offer.query.all()
    return render_template("index.html", gmap=gmap, offers=offers)

@main.route('/new', methods=['GET', 'POST'])
def new_offer():
    form = OfferForm()
    if form.validate_on_submit():
        offer = Offer(currency_from=form.currency_from.data, currency_to=form.currency_to.data,
                      amount=form.amount.data, expires=datetime.now(), latitude=form.latitude.data,
                      longitude=form.longitude.data)
        db.session.add(offer)
        return redirect('/')
    return render_template('new_offer.html', form=form)
