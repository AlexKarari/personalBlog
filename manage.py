
from flask_script import Manager,Server
from app import create_app,db
from app.models import User, Blog, User_comments, Subscription

app = create_app('default')

manager = Manager(app)

manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog, User_comments=User_comments, Subscription=Subscription)

if __name__ == '__main__':
    manager.run()

