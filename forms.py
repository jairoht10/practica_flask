from wtforms import Form 
from wtforms import StringField, TextField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length
from models import Contacts

class SignupForm(Form):
	fullname = StringField('Nombre Completo')
	phone = StringField('Telefono')
	email = EmailField('Email')
	submit = SubmitField('Registrar')


