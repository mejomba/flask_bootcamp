from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup')
def signup_form():
	return render_template('signup_form.html')

@app.route('/thankyou')
def thank_you():
	first = request.args.get('first')
	last = request.args.get('last')
	d = False
	l = False
	u = False
	if first:
		l = any(c.islower() for c in first)
		u = any(c.isupper() for c in first)
		d = first[-1].isdigit()
	else:
		return render_template('signup_form.html', l=l, u=u, d=d)

	# if first[-1].isdigit():
	# 	d = False
	# for i in first:
	# 	if i.islower():
	# 		l = False
	# 	if i.isupper():
	# 		u = False
	if u and l and d:
		return render_template('thank_you.html', first=first, last=last)
	else:
		return render_template('signup_form.html', l=l, u=u, d=d)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', e=e), 404


if __name__ == "__main__":
	app.run(debug=True)