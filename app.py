import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
load_dotenv()
BRIDGE_IP = os.getenv('BRIDGE_IP')
USERNAME = os.getenv('API_USERNAME')

app = Flask(__name__)

@app.route('/trigger/api', methods = ['POST'])
def light_switch():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1/state"
    light_state = get_light_info().get('state', {}).get('on', False)
    print(light_state)
    if light_state == True:
        body = {"on": False}
    else:
        body = {"on": True}
    response = requests.put(url, json=body)
    if response.status_code == 200:
        data = response.status_code
        print(f"Success with code {data}")
    else:
        print(f"Failed: {response.status_code}")



def get_light_info():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed: {response.status_code}")


if __name__ == '__main__':
    app.run(debug  = True)
