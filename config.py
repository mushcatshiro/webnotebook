import os

basedir = os.oth.abspath(os.path.dirname(__file__))

class config:
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or "r4Nd0mS5cRe7"

	@staticmethod
	def init_app(app):
		pass

class DevConfig(config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'data-dev.sqlite')

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