from flask import Flask, request, jsonify
import serial
import os

# Path to the directory containing MicroPython files
micropython_dir = os.path.join(os.path.dirname(__file__), 'micropython_files')

app = Flask(__name__)

# Connect to the serial port (adjust the port name if needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct port name

@app.route('/data', methods=['GET'])
def get_data():
    # Read data from the MicroPython file
    with open(os.path.join(micropython_dir, 'your_micropython_file.py'), 'r') as f:
        data = f.read()

    # Process the data (e.g., parse JSON, extract values)
    # ... your data processing logic here ...

if __name__ == '__main__':
    app.run()