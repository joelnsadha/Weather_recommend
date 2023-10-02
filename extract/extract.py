import requests
import json
from cred import cred
import pandas as pd


class Extracter:
    def __init__(self, lat: str, lon: str):
        """
        Extract weather data from Openweather API.
        :param lat: Str Latitude
        :param lon: Str Longtitude
        """
        self.lat = lat
        self.lon = lon
        self.api_key = cred.api_key

    def get_weather(self):
        """
        Extracts data from API. Returns Pandas Dataframe
        :return: DataFrame
        """

        # Define data fields to extract
        dates = []
        temps = []
        feels_likes = []
        min_temps = []
        max_temps = []
        pressures = []
        sea_level_pressures = []
        grnd_level_pressures = []
        humidities_percent = []
        weather_condition_ids = []
        weather_conditions = []
        condition_descriptions = []
        cloud_conditions = []
        wind_speeds = []
        gusts = []
        visibilities = []
        pops = []
        rain_volumes_3hr = []
        countries = []
        cities = []
        city_ids = []
        populations = []
        timezones = []
        sunrises = []
        sunsets = []

        # Define API URL
        url = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&appid={cred.api_key}"

        # Response from API call
        r = requests.get(url).json()

        # Append field data to predefined lists above
        # list of temp recordings
        items = r.get('list')

        # weather details for each block recording
        for i in items:
            temps.append(i.get('main').get('temp'))
            feels_likes.append(i.get('main').get('feels_like'))
            min_temps.append(i.get('main').get('temp_min'))
            max_temps.append(i.get('main').get('temp_max'))
            pressures.append(i.get('main').get('pressure'))
            sea_level_pressures.append(i.get('main').get('sea_level'))
            grnd_level_pressures.append(i.get('main').get('grnd_level'))
            humidities_percent.append(i.get('main').get('humidity'))

            # Weather conditions
            for condition in i.get('weather'):
                weather_condition_ids.append(condition.get('id'))
                weather_conditions.append(condition.get('main'))
                condition_descriptions.append(condition.get('description'))

            # Cloud conditions
            cloud_conditions.append(i.get('clouds').get('all'))
            wind_speeds.append(i.get('wind').get('speed'))
            gusts.append(i.get('wind').get('gust'))
            visibilities.append(i.get('visibility'))
            pops.append(i.get('pop'))
            if i.get('rain'):
                rain_volumes_3hr.append(i.get('rain').get('3h'))
            else:
                rain_volumes_3hr.append(0)
            dates.append(i.get('dt_txt'))

        countries.append(r.get('city').get('country'))
        cities.append(r.get('city').get('name'))
        city_ids.append(r.get('city').get('id'))
        populations.append(r.get('city').get('population'))
        timezones.append(r.get('city').get('timezone'))
        sunrises.append(r.get('city').get('sunrise'))
        sunsets.append(r.get('city').get('sunset'))

        # Create dataframe features
        features = {
            "date": dates,
            "temp": temps,
            "feels_like": feels_likes,
            "min_temp": min_temps,
            "max_temp": max_temps,
            "pressure": pressures,
            "sea_level_pressure": sea_level_pressures,
            "grnd_level_pressure": grnd_level_pressures,
            "humidity_percent": humidities_percent,
            "weather_condition_id": weather_condition_ids,
            "weather_condition": weather_conditions,
            "condition_description": condition_descriptions,
            "cloud_condition": cloud_conditions,
            "wind_speed": wind_speeds,
            "gust": gusts,
            "visibility": visibilities,
            "pop": pops,
            "rain_volume_3hr": rain_volumes_3hr,
            "city_id": r.get('city').get('id'),
            "longtitude": self.lon,
            "latitude": self.lat,
            "city": r.get('city').get('name'),
            "population": r.get('city').get('population'),
            "timezone": r.get('city').get('timezone')
        }

        # create  pandas dataframe
        df = pd.DataFrame(features)

        return df
