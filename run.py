# coding:utf8
from flask_script import Shell, Manager
from app import create_app
from app import db
from app.model import User
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db=db)


def make_shell_contex():
    return dict(db=db, user=User)


manager.add_command("shell", Shell(make_context=make_shell_contex()))

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
