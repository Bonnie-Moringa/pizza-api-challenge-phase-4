from flask import Flask
from .config import db, migrate
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wandia:#Wandia003@127.0.0.1:5432/restaurants'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

app = create_app()
