#coding:utf8
#create by zhouyao 
#data: $
from . import auth

@auth.route("/")
def auth_slash():
    return "this is frm auth"