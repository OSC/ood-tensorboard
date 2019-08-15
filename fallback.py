from flask import Flask, render_template, flash, redirect
from form import TensorboardForm
import os

MyApp = Flask(__name__)

SECRET_KEY = os.urandom(32)
MyApp.config['SECRET_KEY'] = SECRET_KEY
MyApp.config['APPLICATION_ROOT'] = os.environ['PASSENGER_BASE_URI']

print(os.environ)

@MyApp.route('/', methods=['GET'])
def index():
	form = TensorboardForm()
	if form.validate_on_submit():
		return redirect('/load/')

	return render_template('index.html', title='Create A Tensorboard Instance', form=form) 


if __name__ == "__main__":
	MyApp.run()