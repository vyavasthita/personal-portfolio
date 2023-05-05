from flask import Blueprint, redirect, url_for, render_template
from portfolio.profile.form import ProfileForm


profile_blueprint = Blueprint('profile', __name__, template_folder='templates/profile', static_folder='static')


@profile_blueprint.route('/')
def info():
    return 'Profile Info'

@profile_blueprint.route('/create')
def create_profile():
    form = ProfileForm()

    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data
        email = form.email.data
        phone = form.phone.data
        about_me = form.about_me.data
        dob = form.dob.data

        # Write to DB
        return redirect(url_for('info'))
    return render_template('profile.html', title='Profile', form=form)

