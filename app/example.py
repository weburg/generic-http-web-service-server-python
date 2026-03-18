from datetime import datetime, timezone

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.template_folder = "../templates"
app.static_folder = "../static"

def my_function(name):
    return "Your function knows you as " + name

@app.route("/")
def home():
    request_uri = request.path
    date = datetime.now(timezone.utc)
    return render_template("home.jinja2", request_uri=request_uri, my_function=my_function("Bobcat"), date=date)

@app.route("/generichttpws/", defaults={"path": ""})
@app.route("/generichttpws/<path:path>")
def generichttpws(path):
    request_uri = request.path
    if path == "engines":
        return render_template("generichttpws/engines.jinja2", request_uri=request_uri)

    return render_template("generichttpws/home.jinja2", request_uri=request_uri)

if __name__ == "__main__":
    app.debug = True
    app.run()