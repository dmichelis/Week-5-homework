from flask import Blueprint, render_template, request, flash, redirect, url_for
from homework_car_inventory.forms import UserLoginForm
from homework_car_inventory.models import User, db

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/mycollection')
def my_garage():
    return render_template('mygarage.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data

            print(email,password, first_name, last_name)

            user = User(email, password = password, first_name = first_name, last_name = last_name)
            
            db.session.add(user)
            db.session.commit()
            flash(f'You have successfully created a user account for {email}!, 'user-created')

            return redirect(url_for('main_site.home'))
    
    except:
        raise Exception('Sorry, Invalid Form Data: Please Check Your FOrm Inputs')
    return render_template('signup.html', form = form)

@auth.route('/signin')
def signin():
    return render_template('signin.html')