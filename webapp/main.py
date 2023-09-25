import subprocess
import os, sys

from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path

@app.route('/')
def index():
    return render_template('index.html', version=sys.version, release_info=find_distro())

def find_distro():
    try:
        return subprocess.check_output("cat /etc/*release", shell=True).decode('utf-8')
    except: 
        return "No OS info found"

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)