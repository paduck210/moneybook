from app import app, db
from app.models import Receipt, Usage
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Receipt': Receipt, 'Usage': Usage}
