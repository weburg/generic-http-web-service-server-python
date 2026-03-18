import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "app"))

from example import app
from waitress import serve


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8081)