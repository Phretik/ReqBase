from re import U
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Log
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  ##Finds the user with the email entered
        if user:
            if check_password_hash(user.password, password):  ##Checks password
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)             ##Logs in user
                return redirect(url_for('views.requests'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user, users = User.query.all())

@auth.route('/logout')
@login_required
def logout():           ##Logs out the current user
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/teamLog')
@login_required           ##Renders the team log web page
def teamLog():
    return render_template("team_log.html", user=current_user)


@auth.route('/changePass', methods=['GET', 'POST'])
@login_required
def changePass():
    if request.method =='POST':
        current_Password = request.form.get('currentPassword')
        new_Password1 = request.form.get('Password1')                      ##Captures the form data, then checks if the password entered is correct
        new_Password2 = request.form.get('Password2')
        user = current_user
        if not check_password_hash(user.password, current_Password):
            flash('Incorrect password', category='error')
        else:
            if new_Password1 != new_Password2:
                flash('New password fields do not match', category='error')
            else:
                user.password = generate_password_hash(new_Password1, method='sha256')
                db.session.commit()                                        ##Creates a new hashed password
                flash('Password changed', category='success')
                return redirect(url_for('auth.changePass'))      ##Renders chnage password page
    return render_template("changePass.html", user=current_user)

@auth.route('/account')
@login_required
def account():                     ##Renders the account web page
    return render_template("account.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        password1 = request.form.get('password1')     ##Captures form data
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()   ##Checks if user exists
        if user:
            flash('email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be more than 3 characters.', category='error')
            #pass
        elif len(first_name) < 2:
            flash('Firstname must be more than 1 character.', category='error')   ##Checks data fields to make sure they are valid
            #pass
        elif password1 != password2:
            flash('The passwords do not match.', category='error')
            #pass
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', category='error')
            #pass
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1 , method='sha256'))
            db.session.add(new_user)  ##If a new user, creates a new user and commits to database
            db.session.commit()
            login_user(new_user, remember=True) ##Logs in the user
            # add user to database
            flash('User account created.', category='success')  ##Confirms login
            return redirect(url_for('views.requests'))   ##Renders requests page
            #pass
    return render_template("sign_up.html", user=current_user)  ##If failed, renders the signup page