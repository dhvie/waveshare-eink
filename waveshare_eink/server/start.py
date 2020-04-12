from flask import Flask
from flask import render_template
import datetime as dt
import json
import jinja2 as j2
import requests
import argparse
import os

class OpenWeatherAPI():

    url = j2.Template('https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&appid={{api_key}}&units={{units}}')
    

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

icon_url = j2.Template('http://openweathermap.org/img/wn/{{icon}}{{% if format %}}@{{format}}{{% enif %}}.png')

@app.template_filter()
def icon(value, format='2x'):
    if format == '2x':
        icon_format="2x"
    else:
        icon_format=""
    return icon_url.render(icon=value, format=icon_format)

@app.template_filter()
def format_datetime(value, format='full'):
    if format == 'date':
        dt_format="%d/%m/%Y"
    elif format == 'time':
        dt_format = '%H:%M'
    else:
        dt_format="%d/%m/%Y %H:%M"
    return dt.datetime.fromtimestamp(value).strftime(dt_format)

@app.route('/', methods=['GET'])
@app.route('/<page>', methods=['GET'])
def pages(page=None):
    if page is None:
        page = 'main'
    weather = get_weather()
    return render_template(f'{page}.html', weather=weather)


