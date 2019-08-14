from werkzeug.wsgi import DispatcherMiddleware
from fallback import MyApp
from tensorboard.backend import application as backendWSGI
from tensorboard import default
import tensorflow as tf
import os


def make_app():
    
    return backendWSGI.standard_tensorboard_wsgi(
        assets_zip_provider=default.get_assets_zip_provider(),
        db_uri="",
        logdir="/users/PZS0715/smansour/tensorboardTestbench/logs",
        purge_orphaned_data="",
        reload_interval=5,
        plugins=default.get_plugins(),
        path_prefix=prefix,
        window_title="",
        max_reload_threads=1
        )



application = DispatcherMiddleware(MyApp, {
    '/load': make_app     
})