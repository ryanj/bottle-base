import os
from datetime import datetime
from bottle import Bottle, request, route, run, static_file

app = Bottle()

@app.route('/')
def index():
    return static_file('index.html', root=os.path.realpath('templates'))

@app.route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.realpath('static'))

@app.route("/test")
def test():
    return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    ip = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1')
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
    app.run(host=ip, port=port, debug=True)
