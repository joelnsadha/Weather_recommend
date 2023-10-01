import requests
import json
from cred import cred
import pandas as pd


class Extracter:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.api_key = cred.api_key

    def get_weather(self):
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={cred.api_key}"
        r = requests.get(url)
        return r.json()
