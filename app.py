import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
load_dotenv()
from flask_cors import CORS

BRIDGE_IP = os.getenv('BRIDGE_IP')
USERNAME = os.getenv('API_USERNAME')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/lightswitch/trigger/api', methods = ['PUT'])
def light_switch():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1/state"
    light_state = get_light_info().get('state', {}).get('on', False)
    if light_state == True:
        body = {"on": False}
    else:
        body = {"on": True}
    response = requests.put(url, json=body)
    if response.status_code == 200:
        print(f"Light toggled successfully: {body}")
        return jsonify({"success": True, "new_state": body}), 200
    else:
        print(f"Failed to toggle light: {response.status_code}")
        return jsonify({"success": False, "error": response.status_code}), 500


@app.route('/getlightinfo/trigger/api', methods = ['GET'])
def get_light_info():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed: {response.status_code}")

@app.route('/colorswitch/trigger/api', methods = ['PUT'])
def color_switch():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1/state"
    body = request.json

    response = requests.put(url, json=body)

    if response.status_code == 200:
        print(f"Light toggled successfully: {body}")
        return jsonify({"success": True, "new_state": body}), 200
    else:
        print(f"Failed to toggle light: {response.status_code}")
        return jsonify({"success": False, "error": response.status_code}), 500


if __name__ == '__main__':
    app.run(debug  = True)
