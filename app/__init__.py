from flask import Flask, render_template, redirect, url_for, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from config import config
#from .model import Role

db = SQLAlchemy()
cors = CORS()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
	bootstrap.init_app(app)
	login_manager.init_app(app)

	#Role.insert_roles()

	# attach routes and custom error pages here
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
