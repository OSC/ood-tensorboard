from app import PathDispatcher
from fallback import MyApp
from tensorboard.backend import application as backendWSGI
import tensorflow as tf
import os

tf.flags.DEFINE_boolean(
    'purge_orphaned_data', True, 'Whether to purge data that '
    'may have been orphaned due to TensorBoard restarts. '
    'Disabling purge_orphaned_data can be used to debug data '
    'disappearance.')

tf.flags.DEFINE_integer(
    'reload_interval', 5,
    'How often the backend should load more data, in seconds. Set to 0 to load '
    'just once at startup and a negative number to never reload at all.')

tf.flags.DEFINE_boolean('inspect', False, """Use this flag to print out a digest
of your event files to the command line, when no data is shown on TensorBoard or
the data shown looks weird.
See tensorflow/python/summary/event_file_inspector.py for more info and
detailed usage.
""")

tf.flags.DEFINE_string(
    'path_prefix', '',
    'An optional, relative prefix to the path, e.g. "/path/to/tensorboard". '
    'resulting in the new base url being located at '
    'localhost:6006/path/to/tensorboard under default settings. A leading '
    'slash is required when specifying the path_prefix, however trailing '
    'slashes can be omitted. The path_prefix can be leveraged for path '
    'based routing of an elb when the website base_url is not available '
    'e.g. "example.site.com/path/to/tensorboard/"')

tf.flags.DEFINE_string(
    'window_title', '',
    'The title of the browser window.')

tf.flags.DEFINE_integer(
    'max_reload_threads', 1,
    'The max number of threads that TensorBoard can use to reload runs. Not '
    'relevant for db mode. Each thread reloads one run at a time.')

FLAGS = tf.flags.FLAGS

default_app = MyApp

def make_app(displayLogDir):
	return backendWSGI.standard_tensorboard_wsgi(
		assets_zip_provider="",
		db_uri="",
		logdir=os.path.expanduser(displayLogDir),
		purge_orphaned_data="",
		reload_interval="",
		plugins="",
		path_prefix="",
		window_title="",
		max_reload_threads="",
		flags=FLAGS
		)


application = PathDispatcher(default_app, make_app)

if __name__ == '__main__':
    application.run()