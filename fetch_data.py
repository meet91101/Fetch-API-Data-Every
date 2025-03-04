import requests
import json

# API Endpoint
url = "https://spectator.amnex.com/msrdcgis/layer/getLayerDataByFilter"

# API Request Body
payload = {
    "layer_name": "shp_ecb",
    "chainage_from": 100,
    "chainage_to": 102,
    "control_center": "RTMC-2"
}

# Headers
headers = {
    "Content-Type": "application/json"
}

# Function to fetch data
def fetch_data():
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("Data Fetched:", json.dumps(data, indent=4))
        else:
            print("Error:", response.status_code, response.text)
    except Exception as e:
        print("Exception occurred:", str(e))

if __name__ == "__main__":
    fetch_data()
