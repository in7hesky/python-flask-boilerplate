from flask import Flask
from dynaconf import FlaskDynaconf
import os
from flask import send_from_directory
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    
    with app.app_context():
        FlaskDynaconf(extensions_list=True).init_app(app)
        db.init_app(app)
        
        app.config.SECRET_KEY = bytearray(app.config.SECRET_KEY, "UTF-8")
        
        from . import info
        from . import auth
        
        app.register_blueprint(info.info_bp)
        app.register_blueprint(auth.auth_bp)
        
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                os.path.join(app.root_path, 'static/images'),
                'favicon.ico',
                mimetype='image/vnd.microsoft.icon',
            )
        
        db.create_all()
        
        return app
    

        