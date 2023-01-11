from flask import Flask
from monitor import *

app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/')

def index():
    current_rps = get_rps_current()
    d = {"current_rps":current_rps}
    # return jsonify(d)
    # return str(current_rps)
    return str(judge(current_rps))

app.run(port=8000, debug=True, host="0.0.0.0")