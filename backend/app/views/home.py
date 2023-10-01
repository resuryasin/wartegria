import json
from flask import render_template
import requests

from app import app

@app.route("/")
@app.route("/home")
def index():
    data = []
    getData = (json.loads(requests.get('http://localhost:5001/api/warteg/').json()))
    for i in getData:
        data.append(getData[i])
    return render_template("dashboard.html", data = data)
