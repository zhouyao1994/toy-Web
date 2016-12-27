#coding:utf8
#create by zhouyao 
#data: $

from __future__ import unicode_literals
from flask_wtf import Form
from flask_babel import _
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import  Required,Length,Email

class LoginForm(Form):
    username = StringField(_("username"),validators=[Required(),Length(1,64)])
    password = PasswordField(_("password"),validators=[Required()])
    submit = SubmitField(_("submit"))