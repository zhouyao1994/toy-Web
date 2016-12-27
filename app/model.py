#coding:utf8
#create by zhouyao 
#data: $
from werkzeug.security import generate_password_hash,check_password_hash
from . import db

class User(db.Model):
    ___tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String,unique=True,index=True)
    password = db.Column(db.String)
