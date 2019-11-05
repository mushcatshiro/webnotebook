from flask import Flask, render_template, redirect, url_for, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

db = SQLAlchemy()
cors = CORS()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)
	cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

	# attach routes and custom error pages here
	from .api import api as api_blueprint
	app.register_blueprint(api_blueprint, url_prefix='/api')

	return app
