# coding:utf8
# create by zhouyao
# data: $
from . import main
from ..model import User, db,load_user
from flask_babel import _
from form import LoginForm, RegisterForm
from flask import url_for, render_template, redirect, flash
from flask_login import login_user,logout_user,login_required

# 添加特性一
@main.route('/hello')
def hello_world():
    return 'Hello World!'


@main.route('/hello2')
def hello_world2():
    name = "zhouyao"
    return render_template("index.html", name=name)


@main.route("/login", methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user is not None and user.virify_password(loginForm.password.data):
            login_user(user)
            flash("login success")
    return render_template("login.html", form=loginForm)


@main.route("/register", methods=['GET', 'POST'])
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        user = User(username=registerform.username.data, password=registerform.password.data)
        if not User.query.filter_by(username = registerform.username.data).first():
            db.session.add(user)
            db.session.commit()
            flash("register sucess")
        else:
            flash("has registerec")
    return render_template("register.html", form=registerform)

@main.route("/logout")
@login_required
def log_out():
    logout_user()
    flash("you hava log out")
    return redirect(url_for("main.register"))

@main.route("/get")
@login_required
def get_it():
    print "xxxxx"
    return "this is a private page,should login"