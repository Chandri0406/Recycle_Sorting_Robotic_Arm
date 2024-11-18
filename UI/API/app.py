from flask import Flask, jsonify, send_from_directory
import random
from flask_cors import CORS  # Import Flask-CORS

app = Flask(__name__)
CORS(app, resources={r"/chart-data": {"origins": "http://127.0.0.1:5500"}})
@app.route('/')
def index():
    return send_from_directory('', '../home.html')  # Serve HTML file

@app.route('/app.js')
def serve_js():
    return send_from_directory('', '../scripts/script.js')  # Serve JavaScript file

@app.route('/chart-data')
def chart_data():
    # Generate random values for each category to simulate dynamic data
    data = {
        "Glass": random.randint(10, 50),
        "Metal": random.randint(10, 50),
        "Plastic": random.randint(10, 50),
        "Paper": random.randint(10, 50),
        "Cardboard": random.randint(10, 50),
    }
    return jsonify(list(data.values()))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
