from flask import Blueprint,render_template,flash,url_for,redirect
from flask_login import current_user,login_required

owners = Blueprint('owners',__name__)

@owners.route("/owner")
# @login_required
def owner_dash():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('owner_dash.html',title = 'Owner Dashboard')

@owners.route("/owner/profile")
@login_required
def owner_profile():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('owner_profile.html',title = 'Profile')

@owners.route("/owner/student-list")
@login_required
def student_list():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('student_list.html',title = 'Student List')
