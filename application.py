from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

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
def search();
	return jsonify(ret_value)


if __name__ == '__main__':
	app.run(debug = True)