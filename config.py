import os

class config:
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or "r4Nd0mS5cRe7"

	@staticmethod
	def init_app(app):
		pass

class DevConfig(config):
	DEBUG = True
	# SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

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