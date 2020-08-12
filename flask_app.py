from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = 'mojtaba'
	name_list = list(name)
	name_dict = {"name": 'mojtaba'}
	return render_template('index.html', name=name, name_list=name_list, name_dict=name_dict)


@app.route('/puppy/<name>')
def puppy_latin(name):
	old_name = name
	if name[-1].lower() != 'y':
		name += 'y'
	elif name[-1].lower() == 'y':
		name = name.replace(name[-1], 'iful')
	return render_template('puppy.html', name=name, old_name=old_name)

if __name__ == "__main__":
	app.run(debug=True)