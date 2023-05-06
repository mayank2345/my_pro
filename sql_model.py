from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db_session import app, db





class UserDetails(db.Model):
    s_no = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200), nullable = False)
    name = db.Column(db.String(200), nullable = False)
    email_id = db.Column(db.String(200), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)


with app.app_context():
    db.create_all()