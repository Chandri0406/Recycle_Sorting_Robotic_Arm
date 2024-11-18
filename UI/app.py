from flask import Flask, jsonify, send_from_directory

from flask_cors import CORS  # Import Flask-CORS
from sharedData import materialCounts  # Import from shared_data folder

app = Flask(__name__)
CORS(app, resources={r"/chart-data": {"origins": "http://127.0.0.1:5500"}})
@app.route('/')
def index():
    return send_from_directory('', 'home.html')  # Serve HTML file

@app.route('/app.js')
def serve_js():
    return send_from_directory('', 'scripts/script.js')  # Serve JavaScript file

@app.route('/chart-data')
def chart_data():
    # Generate random values for each category to simulate dynamic data
    data = {category: materialCounts[category] for category in materialCounts}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
