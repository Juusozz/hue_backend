import os
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
load_dotenv()
BRIDGE_IP = os.getenv('BRIDGE_IP')
USERNAME = os.getenv('API_USERNAME')


def get_light_info():
    url = f"http://{BRIDGE_IP}/api/{USERNAME}/lights/1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed: {response.status_code}")


get_light_info()