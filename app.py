from flask import Flask
from config import Config
from models.materia_prima import db
from routes.materia_prima_routes import materia_prima_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(materia_prima_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)