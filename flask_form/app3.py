from flask import Flask, render_template, redirect, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any'

class SimpleForm(FlaskForm):
	breed = StringField('select your breed: ')
	submit = SubmitField('click for flash')

@app.route('/', methods=['GET', 'POST'])
def index3():
	form = SimpleForm()

	if form.validate_on_submit():
		# breed = form.breed.data
		session['breed'] = form.breed.data
		# flash('your select {} breed'.format(breed))
		flash('your select {} breed'.format(session['breed']))
		return redirect(url_for('index3'))

	return render_template('index3.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)