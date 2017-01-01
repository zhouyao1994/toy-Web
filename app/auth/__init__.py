# coding:utf8
# create by zhouyao
# data: $

from flask import Blueprint

# 注意是大写的Bulueprint，不是小写的
auth = Blueprint("auth", __name__)

from . import view
