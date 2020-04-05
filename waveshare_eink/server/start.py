from flask import Flask
from flask import render_template

app = Flask("ws-eink")

@app.route('/<page>', methods=['GET'])
def pages(page=None):
    if page is None:
        page = 'test'
    return render_template(f'{page}.html')
