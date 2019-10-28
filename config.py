import os

class config:
	"""docstring for config"""
	SECRET_KEY = os.environ.get('SECRET_KEY') or "r4Nd0mS5cRe7"

	@staticmethod
	def init_app(app):
		pass

class devConfig(Config):
	DEBUG = True

class TestConfig(Config):
	TESTING = True

class production(Config):
	"""docstring for production"""
	pass

config = {
	'development': devConfig,
	'testing': TestConfig,
	'production': production,
	'default': devConfig
}