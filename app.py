from werkzeug.wsgi import DispatcherMiddleware
from tensorboard.backend import application as backendWSGI
from tensorboard import default
import tensorflow as tf
import os
from werkzeug.wsgi import get_query_string
from flask import request
from threading import Lock
from werkzeug.wsgi import pop_path_info, peek_path_info
from flask import Flask
import pprint
from flask import render_template, flash, redirect
from form import TensorboardForm
import uuid

instances = {}

def create_default_app():
    default_app = Flask(__name__)

    default_app.config['SECRET_KEY'] = os.environ['SECRET_KEY_BASE']
    default_app.config['APPLICATION_ROOT'] = os.environ['PASSENGER_BASE_URI']

    @default_app.route('/', methods=['GET'])
    def index():
        form = TensorboardForm()

        #FIXME: we don't properly handle this
        # instead we modified the target of the form directly
        # to be /load
        # instead we would redirect to /load with the get param passed through
        if form.validate_on_submit():
            return redirect('/load/')

        return render_template('index.html', title='Create A Tensorboard Instance', form=form)

    @default_app.route('/load', methods=['GET'])
    def load():
        key = str(uuid.uuid4())

        instances[key] = create_tb_app(request.args.get("logdir"))

        return redirect('/pun/dev/tensor/instances/' + key + '/')

    return default_app

def create_tb_app(log):

  return backendWSGI.standard_tensorboard_wsgi(
      assets_zip_provider=default.get_assets_zip_provider(),
      db_uri='',
      logdir=os.path.expanduser(log),
      purge_orphaned_data=True,
      reload_interval=5,
      plugins=default.get_plugins(),
      path_prefix='',
      window_title='',
      max_reload_threads=1,
      flags='')


# path dispatcher will accept a reference to an instances map
# but not be responsible for creating new apps
# at this poin

class PathDispatcher(object):
    def __init__(self, default_app, instances):
        self.default_app = default_app
        self.instances = instances

    def __call__(self, environ, start_response):
        my_app = self.instances.get(peek_path_info(environ))

        if my_app is not None:
            pop_path_info(environ)
        else:
            my_app = self.default_app
        return my_app(environ, start_response)

MyApp = create_default_app()

application = DispatcherMiddleware(MyApp, {
    '/instances': PathDispatcher(MyApp, instances)
})
