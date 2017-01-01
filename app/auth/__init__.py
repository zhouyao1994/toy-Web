# coding:utf8
# create by zhouyao
# data: $

from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import view
