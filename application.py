from flask import Flask, render_template, redirect, url_for, jsonify, send_from_directory
from flask_bootstrap import Bootstrap

# app = Flask(__name__)
# app = Flask(__name__, static_folder='client/build')
app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")
Bootstrap(app)

# future scale requires orm?
# form communication with FE react.js
@app.route('/add_post', methods = ['POST'])
def add_post():
	n_post = request.form.get('new_post')
	if n_post:
		# some validation logic need to be implemented
		return render_template(url_for('index'))
	return render_template('add_post.html', )

# to be modified to suit rest api, how to route?
@app.route('/search', methods = ['POST'])
def search():
	return jsonify(ret_value)

@app.route('/')
def index():
        return render_template('index.html')
        # return send_from_directory(app.static_folder, 'index.html')
	# return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True, port = 3003)
