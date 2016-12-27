#coding:utf8
#create by zhouyao 
#data: $
from . import main

@main.route('/hello')
def hello_world():
    return 'Hello World!'