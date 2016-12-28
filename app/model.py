#coding:utf8
#create by zhouyao 
#data: $
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from . import login
from flask_login import UserMixin

class User(UserMixin,db.Model):
    ___tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True,index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self,passw):
        self.password_hash = generate_password_hash(passw)

    def virify_password(self,password):
        return check_password_hash(self.password_hash,password)

@login.user_loader
def load_user(username):
    return User.query.get(username)