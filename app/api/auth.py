from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(userName, password):
	if userName is '':
		return False
	user = user.query.filter_by(userName = userName).first()
	if not user:
		return False
	g.current_user = user
	return user.verify_password(password)
