from flask import Flask
from dynaconf import FlaskDynaconf

def create_app():
    app = Flask(__name__)

    
    with app.app_context():
        FlaskDynaconf(extensions_list=True).init_app(app)
        
        app.config.SECRET_KEY = bytearray(app.config.SECRET_KEY, "UTF-8")
        
        from . import info
        app.register_blueprint(info.info_bp)
        
        return app
    

        