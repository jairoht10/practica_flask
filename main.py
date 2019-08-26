from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from models import db, Contacts
from sqlalchemy import update
import forms
app = Flask(__name__)

# settings
app.secret_key = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/flask'


@app.route('/')
def index():
	signup_form = forms.SignupForm()
	title = "Curso Flask"
	contacts = Contacts.query.all()
	return render_template('index.html', title = title, form = signup_form, contacts=contacts)

@app.route('/add_contact', methods =['GET','POST'])
def add_contact():
	add_contact = forms.SignupForm(request.form)
	if request.method == 'POST':
		contacts = Contacts(id, fullname = add_contact.fullname.data, phone = add_contact.phone.data, email = add_contact.email.data)
		db.session.add(contacts)
		db.session.commit()
		flash('Contacto agregado exitosamente')
		return redirect(url_for('index'))

@app.route('/editar_contact/<id>')
def editar(id):
	signup_form = forms.SignupForm()
	title = "Curso Editar Flask"
	contact = Contacts.query.get(id)
	return render_template('edit-contact.html', title = title, form = signup_form, contact= contact)

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
	if request.method == 'POST':
		contact = Contacts.query.get(id)
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		contact.fullname = fullname
		contact.phone = phone
		contact.email = email
		db.session.commit()
		flash('Contacto actualizado exitosamente')
		return redirect(url_for('index'))

@app.route('/delete_contact/<string:id>')
def detele(id):
	contact = Contacts.query.filter_by(id= id).first()
	db.session.delete(contact)
	db.session.commit()
	flash('Contacto eliminado exitosamente')
	return redirect(url_for('index'))

	#return id


if __name__ == '__main__':
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True, port=8000)