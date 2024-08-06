from flask import Flask
from dynaconf import FlaskDynaconf

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        FlaskDynaconf().init_app(app)
        
        from . import info
        app.register_blueprint(info.info_bp)
        
        return app
    

        