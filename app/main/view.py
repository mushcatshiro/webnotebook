from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user
from . import main
from ..model import kPost, User
from .. import db
from ..forms import RegistrationForm, LoginForm


status_green = "complete"

@main.route('/post/<int:userId>', methods=['GET' ,'POST'])
@login_required
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

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userName=form.userName.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            flash('success')
            return redirect(next)
        flash('Invalid email or password.')
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you are not logged out')
    return redirect(url_for('main.index'))

@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')