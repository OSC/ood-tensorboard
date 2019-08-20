from werkzeug.wsgi import DispatcherMiddleware
from fallback import MyApp
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


#print(get_query_string(environ))
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


def create_dummy_app(details):
  app = Flask(__name__, instance_relative_config=True)

  @app.route('/')
  def index():
      return "<h2>" + ("/") + "</h2><pre>" + details + "</pre>"

  @app.route('/<path:subpath>')
  def index_with_subpath(subpath):
      return "<h2>" + (subpath or "None") + "</h2><pre>" + details + "</pre>"

  return app

# path dispatcher will accept a reference to an instances map
# but not be responsible for creating new apps

class PathDispatcher(object):
    def __init__(self, default_app, instances):
        self.default_app = default_app
        self.instances = instances

    def __call__(self, environ, start_response):
        # my_app = pprint.pformat(self.instances.get(peek_path_info(environ)))
        my_app = create_dummy_app(pprint.pformat(self.instances) +
                                  "\n\npeek_path_info: " +
                                  peek_path_info(environ) + "\n\napp found:" + pprint.pformat(self.instances.get(peek_path_info(environ))))

        if my_app is not None:
            pop_path_info(environ)
        else:
            my_app = self.default_app
        return my_app(environ, start_response)

application = DispatcherMiddleware(MyApp, {
    '/instances': PathDispatcher(MyApp, {
        'one': create_tb_app("/users/PZS0715/smansour/TensorboardTestbench/logs/"),
        'two': create_tb_app("/users/PZS0562/efranz/tmp/TensorboardTestbench/logs/")
    })
})
