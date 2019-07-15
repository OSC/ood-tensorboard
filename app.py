from flask import Flask, render_template

MyApp = Flask(__name__)

from werkzeug.wsgi import DispatcherMiddleware
from tensorboard import program, default

appOne = program.create_tb_app(default.get_plugins(), default.get_assets_zip_provider())
appTwo = program.create_tb_app(default.get_plugins(), default.get_assets_zip_provider())

application = DispatcherMiddleware(MyApp, {
    '/appone':    appOne,
    '/apptwo':    appTwo
})



if __name__ == "__main__":
	MyApp.run()