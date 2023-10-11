import json
from flask import render_template, request, jsonify
import requests

from app import app
from app.config import BASE_URL

@app.route("/")
@app.route("/home")
def index():
    try:
        response = requests.get(f'{BASE_URL}/api/warteg/')
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, (list, tuple)):
            raise ValueError("API response is not a list or tuple")
    except requests.exceptions.RequestException as e:
        error_message = f"Error making API request: {e}"
    except (json.JSONDecodeError, ValueError) as e:
        error_message = f"Error parsing API response: {e}"
    except Exception as ex:
        error_message = f"Unexpected error: {ex}"
    else:
        error_message = None
            
    if error_message:
        data = []
        app.logger.error(error_message)

    return render_template("dashboard.html", data=data, BASE_URL=BASE_URL)
