from flask import Flask, render_template
from requests import post, get
import json

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    data = []
    getData = (json.loads(get('http://localhost:5001/api/warteg/').json()))
    for i in getData:
        data.append(getData[i])
    return render_template("dashboard.html", data = data)

app.run(host="127.0.0.1", debug=True)

