from app import PathDispatcher
from fallback import MyApp
from tensorboard.backend import application as backendWSGI
from tensorboard import default
import tensorflow as tf
import os


default_app = MyApp

def make_app():
	return backendWSGI.standard_tensorboard_wsgi(
		assets_zip_provider=default.get_assets_zip_provider(),
		db_uri="",
		logdir=os.path.expanduser("/users/PZS0715/smansour/tensorboardTestbench/logs"),
		purge_orphaned_data=true,
		reload_interval=5,
		plugins=default.get_plugins(),
		path_prefix="",
		window_title="",
		max_reload_threads=1
		)


application = PathDispatcher(default_app, make_app)

if __name__ == '__main__':
    application.run()