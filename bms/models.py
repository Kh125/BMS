from bms import db,loginmanager
from flask_login import UserMixin

@loginmanager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(100),nullable = False)
  password = db.Column(db.String(60),nullable = False)
  email = db.Column(db.String(100),nullable = False,unique=True)
  usertype = db.Column(db.Boolean,nullable = False)

  def __repr__(self):
    return f"User('{self.name}','{self.password}','{self.email}','{self.usertype}')"


    