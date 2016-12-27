#coding:utf8
from flask_script import Shell,Manager
from app import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()