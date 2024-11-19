import random
import time
import requests

def simulate_detection():
    """Simulate detection of materials periodically."""
    materials = ['glass', 'metal', 'plastic', 'paper', 'cardboard']
    url = 'http://127.0.0.1:5000/update-material'

    while True:
        detected_material = random.choice(materials)
        try:
            response = requests.post(url, json={'material': detected_material})
            if response.status_code == 200:
                print(f"Successfully updated count for {detected_material}")
            else:
                print(f"Failed to update count for {detected_material}: {response.text}")
        except requests.RequestException as e:
            print(f"Error connecting to update service: {e}")

        # Wait 3 seconds between updates
        time.sleep(3)

if __name__ == "__main__":
    simulate_detection()
