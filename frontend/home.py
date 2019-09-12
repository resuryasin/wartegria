from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/urut", methods=["GET"])
def urut():
    return render_template("sort.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)

