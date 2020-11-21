from flask import Blueprint,render_template,redirect,flash,url_for,request
from bms.main.forms import LoginForm,RegisterForm
from bms.models import User
from bms import db,bcrypt
from flask_login import login_user,logout_user,current_user

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
  return render_template('index.html',title='Home')

@main.route("/about")
def about():
  return render_template('about.html',title='About')

@main.route("/contact")
def contact():
  return render_template('contact.html',title='Contact')

@main.route("/school-list")
def feedback():
  return render_template('school_list.html',title='School List')

@main.route("/login",methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
    flash(f'Already authenticated','danger')
    return redirect(url_for('main.home'))
  forms = LoginForm()
  if forms.validate_on_submit():
    user = User.query.filter_by(email=forms.email.data).first()
    if user and bcrypt.check_password_hash(user.password,forms.password.data):
      login_user(user)
      flash(f'Login success (db)!','success')
      req_page = request.args.get('next')
      if user.usertype == 1:
        return redirect(req_page) if req_page else redirect(url_for('owners.owner_dash'))
      return redirect(req_page) if req_page else redirect(url_for('parents.parent_dash'))
    else:
      flash(f'Incorrect username or password!','danger')
  return render_template('login.html',title='Login',forms = forms)

@main.route("/register",methods=['GET','POST'])
def register():
  if current_user.is_authenticated:
    flash(f'Already authenticated','danger')
    return redirect(url_for('main.home'))
  forms = RegisterForm()
  if forms.validate_on_submit():  
    if request.form.get('check_type') == '1':
      user_type_data = 1
    else:
      user_type_data = 0
    hash_password = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
    user = User(name=forms.username.data,password=hash_password,email=forms.email.data,usertype=user_type_data)
    db.session.add(user)
    db.session.commit()
    flash(f'Registeration success.You can login now!','success')
    return redirect(url_for('main.login'))  
    
  return render_template('register.html',title = 'Register',forms = forms)



@main.route("/logout")
def logout():
  logout_user()
  flash(f'Logout success','success')
  return redirect(url_for('main.home'))