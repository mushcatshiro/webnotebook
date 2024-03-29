import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# /home/mushcat/webnotebook

class config:
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or "r4Nd0mS5cRe7"
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	REMEMBER_COOKIE_DURATION = 86400

	@staticmethod
	def init_app(app):
		pass

class DevConfig(config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///data-dev.db'

class TestConfig(config):
	TESTING = True

class Production(config):
	"""docstring for production"""
	pass

config = {
	'development': DevConfig,
	'testing': TestConfig,
	'production': Production,
	'default': DevConfig
}