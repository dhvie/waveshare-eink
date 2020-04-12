from flask import Flask
from flask import render_template
import json
import jinja2 as j2
import requests
import argparse
import os

class OpenWeatherAPI():

    url = j2.Template('https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&appid={{api_key}}&units={{units}}')
    icon_url = j2.Template('http://openweathermap.org/img/wn/{{icon}}@2x.png')

    def __init__(self, api_key):
        self.__api_key = api_key

    def call(self, lon, lat, units='imperial'):
        return json.loads(requests.get(OpenWeatherAPI.url.render(api_key=self.__api_key, lon=lon, lat=lat, units=units)).text)

    def get_icon_url(self, icon):
        return OpenWeatherAPI.icon_url.render(icon=icon)

args = {
    'own': os.environ['OWN_API'],
    'lon': os.environ['LON'],
    'lat': os.environ['LAT']
}

app = Flask("ws-eink")

own_api = OpenWeatherAPI(args['own'])

def get_weather():
    return own_api.call(args['lon'], args['lat'])

@app.route('/', methods=['GET'])
@app.route('/<page>', methods=['GET'])
def pages(page=None):
    if page is None:
        page = 'main'
    weather = get_weather()
    weather_icon = own_api.get_icon_url(weather['current']['weather'][0]['icon'])
    return render_template(f'{page}.html', weather=weather, weather_icon=weather_icon)


