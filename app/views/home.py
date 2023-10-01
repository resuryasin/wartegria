import json
from flask import render_template
import requests

from app import app
from app.config import BASE_URL

@app.route("/")
@app.route("/home")
def index():
    data = []
    getData = (json.loads(requests.get(f'{BASE_URL}/api/warteg/').json()))
    for i in getData:
        data.append(getData[i])
    return render_template("dashboard.html", data = data)
