from flask import render_template, redirect, url_for, flash
from . import main
from ..model import kPost, User
from .. import db
from ..forms import RegistrationForm


status_green = "complete"

@main.route('/post/<int:userId>', methods=['GET' ,'POST'])
def get_userPost(userId):
    kPost_ = kPost() 
    userPost = kPost_.display_userPost(userId=userId)
    return jsonify(userPost)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(userName=form.userName.data, email=form.email.data.lower(), password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account',
        #            'auth/email/confirm', user=user, token=token)
        # flash('A confirmation email has been sent to you by email.')
        flash('success')
        return redirect(url_for('.index'))
    return render_template('register.html', form=form)

@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')