from flask import Flask
from dynaconf import FlaskDynaconf
import os
from flask import send_from_directory

def create_app():
    app = Flask(__name__)

    
    with app.app_context():
        FlaskDynaconf(extensions_list=True).init_app(app)
        
        app.config.SECRET_KEY = bytearray(app.config.SECRET_KEY, "UTF-8")
        
        from . import info
        app.register_blueprint(info.info_bp)
        
        @app.route('/favicon.ico')
        def favicon():
            return send_from_directory(
                os.path.join(app.root_path, 'static/images'),
                'favicon.ico',
                mimetype='image/vnd.microsoft.icon',
            )
            
        return app
    

        