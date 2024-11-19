from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE_PATH = 'UI\scripts\data.json'

def load_data():
    """Load data from the JSON file."""
    if os.path.exists(DATA_FILE_PATH):
        try:
            with open(DATA_FILE_PATH, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON. Resetting data.")
            return {"glass": 0, "metal": 0, "plastic": 0, "paper": 0, "cardboard": 0}
    else:
        # Default data structure if file doesn't exist
        return {"glass": 0, "metal": 0, "plastic": 0, "paper": 0, "cardboard": 0}

def save_data(data):
    """Save data to the JSON file."""
    try:
        with open(DATA_FILE_PATH, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error saving data: {e}")

@app.route('/update-material', methods=['POST'])
def update_material():
    """Handles updates to material counts."""
    try:
        data = request.json
        material_type = data.get('material')

        valid_materials = ["glass", "metal", "plastic", "paper", "cardboard"]
        if material_type not in valid_materials:
            return jsonify({"error": "Invalid material type"}), 400

        # Load, update, and save data
        current_data = load_data()
        current_data[material_type] += 1
        save_data(current_data)

        return jsonify({"message": f"Updated {material_type} count"}), 200
    except Exception as e:
        print(f"Error updating material count: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":

    app.run(debug=False, use_reloader=False)