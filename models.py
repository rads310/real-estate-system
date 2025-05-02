from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=False)
    area = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='available')
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    client_type = db.Column(db.String(50))  # owner, buyer, renter
    
class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contract_type = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    date = db.Column(db.Date, nullable=False)
    
class Inspection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    inspection_date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    market_price = db.Column(db.Float)