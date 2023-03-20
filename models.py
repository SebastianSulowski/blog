from . import db
import datetime

class Entry(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(80), nullable=False)
   body = db.Column(db.Text, nullable=False)
   pub_date = db.Column(db.DateTime, nullable=False,
       default=datetime.datetime.utcnow)
   is_published = db.Column(db.Boolean, default=False)

FLASK_APP=blog flask db init

FLASK_APP=blog flask db migrate -m "Add Post table"

FLASK_APP=blog flask db upgrade