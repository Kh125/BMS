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

@owners.route("/owner/car-list")
@login_required
def car_list():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('car_list.html',title = 'Car List')

@owners.route("/owner/student-list")
@login_required
def student_list():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('student_list.html',title = 'Student List')

@owners.route("/owner/car-info")
@login_required
def car_info():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('car_info.html',title = 'Car Info')

@owners.route("/owner/add")
@login_required
def add_car():
  if current_user.usertype == 0:
    flash(f'You can\'t access this page','danger')
    return redirect(url_for('parents.parent_dash'))
  return render_template('add_car.html',title = 'New Car')
