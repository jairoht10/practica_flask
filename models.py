from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Contacts(db.Model):
	__tablaname__ = 'contacts'
	id = db.Column(db.Integer, primary_key = True)
	fullname = db.Column(db.String(50))
	phone = db.Column(db.String(50))
	email = db.Column(db.String(50))

	def __init__(self, id, fullname, phone, email):
		self.id = id
		self.fullname = fullname
		self.phone = phone
		self.email = email