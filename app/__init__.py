# app/__init__.py
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE='app.db'  # Utiliser un fichier au lieu de :memory:
        )
    
    # Le reste du code reste inchangé
    from app.api import api_bp
    app.register_blueprint(api_bp)
    
    @app.route('/')
    def index():
        return "L'application fonctionne. Essayez /api/add/2/3"
    
    return app