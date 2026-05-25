import json
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone

from flask import Flask, render_template, request

from app.domain.omnibus import Omnibus
from app.my_function import my_function


def json_default(value):
    if isinstance(value, datetime):
        return value.isoformat(timespec="milliseconds")

    if is_dataclass(value):
        return asdict(value)

    raise TypeError(f"Object of type {value.__class__.__name__} is not JSON serializable")


app = Flask(__name__)
app.template_folder = "../templates"
app.static_folder = "../static"

@app.route("/")
def home():
    date = datetime.now(timezone.utc)
    request_uri = request.path
    return render_template("home.jinja2", request_uri=request_uri, my_function=my_function, date=date)

@app.route("/generichttpws/", defaults={"path": ""})
@app.route("/generichttpws/<path:path>")
def generichttpws(path):
    request_uri = request.path
    if path == "engines":
        return render_template("generichttpws/engines.jinja2", request_uri=request_uri)
    elif path == "omnibus":
        omnibus = Omnibus()
        omnibus.birthtime = datetime.fromisoformat("2016-05-11T12:00:00.000")
        omnibus.sendtime = datetime.now(timezone.utc)
        omnibus.toppings = ["Cheese", "Pepperoni", "Sausage"]
        omnibus.sides = ["Fries", "Onion Rings"]
        omnibus.onFire = False
        omnibus.document = None
        omnibus.pairing = {
            "Steak": "Cabernet Sauvignon",
            "Fish": "Chardonnay",
        }

        return json.dumps(omnibus, default=json_default)

    return render_template("generichttpws/home.jinja2", request_uri=request_uri)

if __name__ == "__main__":
    app.debug = True
    app.run()