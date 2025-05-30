from flask import Flask, request, send_file
from datetime import datetime
from io import BytesIO

app = Flask(__name__)

# Create a 1x1 transparent PNG
pixel_data = bytes([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A,
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52,
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01,
    0x08, 0x06, 0x00, 0x00, 0x00, 0x1F, 0x15, 0xC4,
    0x89, 0x00, 0x00, 0x00, 0x0A, 0x49, 0x44, 0x41,
    0x54, 0x78, 0x9C, 0x63, 0x60, 0x00, 0x00, 0x00,
    0x02, 0x00, 0x01, 0xE5, 0x27, 0xD4, 0xA2, 0x00,
    0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE,
    0x42, 0x60, 0x82
])

@app.route('/track')
def track():
    # Get the real IP from proxy header, fallback to remote_addr
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log to file
    with open('logs.txt', 'a') as f:
        f.write(f"{time_now} - IP: {ip} - UA: {user_agent}\n")

    print(f"🔥 Beacon hit! IP: {ip}")

    # Return the 1x1 invisible PNG
    return send_file(BytesIO(pixel_data), mimetype='image/png')

@app.route('/')
def home():
    return '👁️‍🗨️ Tracking Pixel Server is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
