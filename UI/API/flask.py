from flask import Flask, request, jsonify
import serial
import os

# Path to the directory containing MicroPython files
micropython_dir = os.path.join(os.path.dirname(__file__), 'micropython_files')

app = Flask(__name__)
ser = None;

# Connect to the serial port (adjust the port name if needed)
try:
  ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the correct port name
except serial.SerialException as e:
  print(f"Error connecting to serial port: {e}")
  exit(1)


@app.route('/data', methods=['GET'])
def get_data():
  try:
    # Read data from the MicroPython file
    with open(os.path.join(micropython_dir, 'your_micropython_file.py'), 'r') as f:
      data = f.read()

    # Process the data (e.g., parse JSON, extract values)
    # ... your data processing logic here ...

    # Return processed data (replace with your actual logic)
    return jsonify({'data': data})
  except FileNotFoundError:
    # Handle case where file is not found
    return jsonify({'error': 'Micropython file not found'}), 404
  except Exception as e:  # Catch generic exceptions
    # Log the error for debugging
    print(f"Error getting data: {e}")
    # Return generic error message to user
    return jsonify({'error': 'An error occurred'}), 500


if __name__ == '__main__':
  app.run()