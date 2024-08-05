from flask import Flask, render_template
from random import randint

def create_app():
    app = Flask(__name__)
    
    with app.app_context():
        
        @app.route("/")
        def home():
            return render_template("index.html", 
                            data={
                                "random_integer": randint(0, 10),
                                "visits_counter": VisitsCounter(),
                                })
        
        return app
    
class VisitsCounter:
    COUNT = 0
    
    def increment(self):
        VisitsCounter.COUNT += 1
        return VisitsCounter.COUNT
        