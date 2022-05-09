from app import create_app,db
from flask_script import Manager,Shell,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Runs the unit tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User, Role = Role)

if __name__ == '__main__':
    manager.run()