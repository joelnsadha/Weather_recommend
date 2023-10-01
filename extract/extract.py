import requests
import json
from cred import cred
import pandas as pd


def get_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={cred.api_key}"
    r = requests.get(url)
    return r.json()
