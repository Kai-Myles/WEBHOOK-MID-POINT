from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/track')
def track():
    with open('logs.txt', 'a') as f:
        f.write(f"\n{datetime.now()} - IP: {request.remote_addr} - UA: {request.headers.get('User-Agent')}")
    return send_file('1x1.png', mimetype='image/png')

app.run(host='0.0.0.0', port=5000)
