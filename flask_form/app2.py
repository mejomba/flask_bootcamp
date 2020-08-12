from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
					SubmitField, TextAreaField, TextField,
					RadioField, SelectField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any'

class InfoForm(FlaskForm):
	breed = StringField('what breed are you?', validators=[DataRequired()])
	neutered = BooleanField('have you been neutered?')
	mood = SelectField('select your mood: ', choices=[('h', 'happy'), ('a', 'angry')])
	food_choice = SelectField('select favorite food', choices=[('f', 'fish'),
																 ('c', 'chicken'),
																 ('b', 'beef') ])
	feedback = TextAreaField()
	submit = SubmitField('submit')
	testtext = TextField('this is test: ')


@app.route('/', methods=['GET', 'POST'])
def index2():
	form = InfoForm()

	if form.validate_on_submit():
		session['breed'] = form.breed.data 
		session['neutered'] = form.neutered.data 
		session['mood'] = form.mood.data
		session['food_choice'] = form.food_choice.data 
		session['feedback'] = form.feedback.data 
		session['testtext'] = form.testtext.data 

		return redirect(url_for('thankyou'))

	return render_template('index2.html', form=form)

@app.route('/thank_you')
def thankyou():
	return render_template('thankyou.html')

if __name__ == '__main__':
	app.run(debug=True)







