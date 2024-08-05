from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", 
                           data={
                               "random_integer": randint(0, 10),
                               "visits_counter": VisitsCounter(),
                               })

class VisitsCounter:
    COUNT = 0
    
    def increment(self):
        VisitsCounter.COUNT += 1
        return VisitsCounter.COUNT
        