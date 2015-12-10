from datetime import datetime

from flask.ext.googlemaps import Map
from flask.ext.login import login_required, current_user

from flask import render_template, redirect
from . import main
from .forms import OfferForm
from ..models import Offer
from .. import db

@main.route('/')
def index():
    offers = Offer.query.all()
    markers = [(o.latitude, o.longitude) for o in offers]

    gmap = Map(identifier="view-side",
               lat=49.22573,
               lng=16.58205,
               markers=markers,
               style="height:600px;width:100%;")
    return render_template("index.html", gmap=gmap, markers=markers, offers=offers)

@main.route('/new', methods=['GET', 'POST'])
@login_required
def new_offer():
    form = OfferForm()
    if form.validate_on_submit():
        offer = Offer(currency_from=form.currency_from.data,
                      currency_to=form.currency_to.data,
                      amount=form.amount.data,
                      expires=datetime.now(),
                      latitude=form.latitude.data,
                      longitude=form.longitude.data,
                      owner_id=current_user.id)
        db.session.add(offer)
        return redirect('/')
    return render_template('new_offer.html', form=form)

@main.route('/propose/<offer_id>', methods=['GET', 'POST'])
@login_required
def propose_offer(offer_id):
    form = OfferForm()
    my_offers = current_user.offers
    return render_template('propose_offer.html', my_offers=my_offers, form=form)
