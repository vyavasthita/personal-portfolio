from flask import Blueprint, render_template, flash, url_for, redirect
from portfolio.user.forms import UserRegisterForm
from portfolio.dao import user_dao


user_blueprint = Blueprint('user', __name__, template_folder='templates/user')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.username.data
        password = form.username.data
        password_repeat = form.username.data

        user_dao.create_user(username=username, email=email, password=password)
        return redirect(url_for('user.register_info'))

    return render_template('register.html', title='User Registration', form=form)


@user_blueprint.route('/registe_info')
def register_info():
    return 'Registration Successful'