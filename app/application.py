from flask import Flask, render_template, redirect, url_for, jsonify, session
from . import kPost, user

app = Flask(__name__)


status_green = "complete"

@app.route('/post/<int:userId>', methods=['GET' ,'POST'])
def get_userPost(userId):
    kPost_ = kPost() 
    userPost = kPost_.display_userPost(userId=userId)
    return jsonify(userPost)

@app.route('/createuser', methods=['POST'])
def get_userPost():
    kPost_ = kPost() 
    userPost = kPost_.display_userPost(userId=userId)
    return render_template('index.html', form = form)
if __name__ == '__main__':
	app.run(debug = True)
