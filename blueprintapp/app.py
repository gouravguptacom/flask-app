from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprint.db'

    db.init_app(app)

    # import and register all blueprint
    from blueprintapp.blueprints.cores.routes import cores
    from blueprintapp.blueprints.todos.routes import todos
    from blueprintapp.blueprints.peoples.routes import peoples

    app.register_blueprint(cores)
    app.register_blueprint(todos, url_prefix="/todos")
    app.register_blueprint(peoples, url_prefix="/peoples")

    migrate = Migrate(app, db)

    return app