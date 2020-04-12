from flask import Flask
from flask import render_template
import datetime as dt
import json
import jinja2 as j2
import requests
import argparse
import os
import feedparser

class OpenWeatherAPI():

    url = j2.Template('https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&appid={{api_key}}&units={{units}}')
    

    def __init__(self, api_key):
        self.__api_key = api_key

    def call(self, lon, lat, units='imperial'):
        return json.loads(requests.get(OpenWeatherAPI.url.render(api_key=self.__api_key, lon=lon, lat=lat, units=units)).text)

args = {
    'own': os.environ['OWN_API'],
    'lon': os.environ['LON'],
    'lat': os.environ['LAT']
}

app = Flask("ws-eink")

own_api = OpenWeatherAPI(args['own'])

def get_weather():
    return own_api.call(args['lon'], args['lat'])

def get_news():
    bbc_rss = "http://feeds.bbci.co.uk/news/rss.xml?edition=uk"
    feed = feedparser.parse( bbc_rss )
    return feed

icon_map = {
    '01': '<span class="material-icons">wb_sunny</span>',
    '02': '<span class="material-icons">wb_cloudy</span>',
    '03': '<span class="material-icons">wb_cloudy</span>',
    '04': '<span class="material-icons">wb_cloudy</span>',
    '09': '<img src="/icons/rain" />',
    '10': '<img src="/icons/rain" />',
    '11': '<span class="material-icons">flash_on</span>',
    '13': '<span class="material-icons">ac_unit</span>',
    '50': '<img src="/icons/fog" />'
}

@app.template_filter()
def icon(value):
    material = icon_map.get(value[:2], "")
    return material

@app.template_filter()
def format_datetime(value, format='full'):
    if format == 'date':
        dt_format="%d/%m/%Y"
    elif format == 'time':
        dt_format = '%H:%M'
    else:
        dt_format="%d/%m/%Y %H:%M"
    return dt.datetime.fromtimestamp(value).strftime(dt_format)


@app.route('/icons/<name>', methods=['GET'])
def get_icons(name):
    with open(f'./icons/{name}.svg') as icon:
        icon_str = icon.read()

    return icon_str


@app.route('/', methods=['GET'])
@app.route('/<page>', methods=['GET'])
def pages(page=None):
    if page is None:
        page = 'main'
    weather = get_weather()
    feed = get_news()
    return render_template(f'{page}.html', weather=weather, news=feed)


