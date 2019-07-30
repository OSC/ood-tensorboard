from flask import Flask, render_template, flash, redirect
from form import TensorboardForm
import os

MyApp = Flask(__name__)
MyApp.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@MyApp.route('/', methods=['GET', 'POST'])
def index():
	form = TensorboardForm()
	if form.validate_on_submit():
		flash('Instance requested for log directory: {}'.format(form.logdir.data))
		pathPrefix = form.path.data
		return redirect('/%s/') % (pathPrefix)

	return render_template('index.html', title='Create A Tensorboard Instance', form=form) 


if __name__ == "__main__":
	MyApp.run()