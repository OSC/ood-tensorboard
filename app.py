from werkzeug.wsgi import DispatcherMiddleware
from fallback import MyApp
from tensorboard.backend import application as backendWSGI
from tensorboard import default
import tensorflow as tf
import os
from werkzeug.wsgi import get_query_string
from tensorboard.backend import application
from flask import request


print(get_query_string(environ))
def create_tb_app(plugins, assets_zip_provider, log="/users/PZS0715/smansour/TensorboardTestbench/logs/"):

  return application.standard_tensorboard_wsgi(
      assets_zip_provider=assets_zip_provider,
      db_uri='',
      logdir=os.path.expanduser(log),
      purge_orphaned_data=True,
      reload_interval=5,
      plugins=plugins,
      path_prefix='',
      window_title='',
      max_reload_threads=1,
      flags='')


application = DispatcherMiddleware(MyApp, {
    '/load': create_tb_app(default.get_plugins(), default.get_assets_zip_provider(), )     
})