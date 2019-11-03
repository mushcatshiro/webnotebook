from flask import Flask, render_template, redirect, url_for, jsonify, send_from_directory
# from flask_sqlalchemy import SQLAlchemy
from config import config

# db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	# db.init_app(app)

	# attach routes and custom error pages here
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')

	return app
