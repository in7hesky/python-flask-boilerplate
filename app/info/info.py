from flask import render_template
from random import randint
from . import info_bp

@info_bp.route("/")
def home():
    return render_template("index.html", 
                    data={
                        "random_integer": randint(0, 10),
                        "visits_counter": VisitsCounter(),
                        })

@info_bp.route("/about")
def about():
    return render_template("about.html")

class VisitsCounter:
    COUNT = 0
    
    def increment(self):
        VisitsCounter.COUNT += 1
        return VisitsCounter.COUNT