#!/usr/bin/python3

import os
from app import create_app, db
from app.models import Offer
from flask.ext.script import Manager, Shell

app = create_app(os.getenv("WTT_FLASK_CONFIG") or "default")
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Offer=Offer)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
