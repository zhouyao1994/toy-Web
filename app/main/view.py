#coding:utf8
#create by zhouyao 
#data: $
from . import main
from ..model import User
from flask_babel import _
from form import LoginForm
from flask import url_for,render_template,redirect,flash

@main.route('/hello')
def hello_world():
    return 'Hello World!'

@main.route('/hello2')
def hello_world2():
    name = "zhouyao"
    return render_template("index.html",name = name)


@main.route("/login")
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(email=loginForm.email.data).first()
        if user is not None and user.password == loginForm.password.data:
            flash(_("login success"))
    return render_template("login.html",form = loginForm)