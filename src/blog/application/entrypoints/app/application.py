from flask import Flask

from blog.application.entrypoints.app.blueprints.auth import blueprint as user_blueprint
from blog.application.entrypoints.app.blueprints.blog import blueprint as blog_blueprint
from blog.configurator.config import init_app
from blog.configurator.containers import Container


def create_app() -> Flask:
    app = Flask(__name__)
    container = Container()
    app.secret_key = "patrick"
    app.container = container
    with app.app_context():
        init_app(app)
    app.register_blueprint(blog_blueprint)
    app.register_blueprint(user_blueprint)
    app.add_url_rule("/", endpoint="index")
    return app
