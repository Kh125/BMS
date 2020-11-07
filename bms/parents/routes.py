from flask import Blueprint,render_template,flash,redirect,url_for
from flask_login import current_user

parents = Blueprint('parents',__name__)

@parents.route("/parent")
def parent_dash():
  if current_user.usertype == 1:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('owners.owner_dash'))
  return render_template('parent_dash.html',title = 'Parent Dashboard')

@parents.route("/parent/profile")
def parent_profile():
  if current_user.usertype == 1:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('owners.owner_dash'))
  return render_template('parent_profile.html',title = 'Profile')