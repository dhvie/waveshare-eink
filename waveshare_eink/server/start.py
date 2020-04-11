from flask import Flask
from flask import render_template
import jinja2 as j2
import requests
import argparse
import os

class OpenWeatherAPI():

    url = j2.Template('https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&appid={{api_key}}&units={{units}}')

    def __init__(self, api_key):
        self.__api_key = api_key

    def call(self, lon, lat, units='imperial'):
        return requests.get(url.render(api_key=self.__api_key, lon=lon, lat=lat, units=units))


args = {
    'own': os.environ['OWN_API'],
    'lon': os.environ['LON'],
    'lat': os.environ['LAT']
}

app = Flask("ws-eink")

own_api = OpenWeatherAPI(args.own)

@app.route('/<page>', methods=['GET'])
def pages(page=None):
    if page is None:
        page = 'main'
    return render_template(f'{page}.html')


@app.route('/weather', methods=['GET'])
def weather():
    result = own_api.call(args.lon, args.lat)

