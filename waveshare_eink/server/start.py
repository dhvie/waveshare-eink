from flask import Flask
from flask import render_template
import jinja2 as j2
import requests
import argparse

class OpenWeatherAPI():

    url = j2.Template('https://api.openweathermap.org/data/2.5/onecall?lat={{lat}}&lon={{lon}}&appid={{api_key}}')

def main(args):
    app = Flask("ws-eink")

    @app.route('/<page>', methods=['GET'])
    def pages(page=None):
        if page is None:
            page = 'main'
        return render_template(f'{page}.html')


    @app.route('/weather', methods=['GET'])
    def weather():
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--own", type=str)
    args = parser.parse_args()
    main(args)
