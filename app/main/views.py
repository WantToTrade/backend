from flask.ext.googlemaps import Map

from flask import render_template
from . import main
from .forms import OfferForm
from .. import db

@main.route('/')
def index():
    gmap = Map(identifier="view-side",
               lat=49.22573,
               lng=16.58205,
               style="height:600px;width:100%;")
    return render_template("index.html", gmap=gmap, offers=[])

@main.route('/new', methods=['GET', 'POST'])
def new_offer():
    form = OfferForm()
    return render_template('new_offer.html', form=form)
