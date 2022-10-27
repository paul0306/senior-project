#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from flask import Flask, request, render_template, request
import control as c

# init
app = Flask(__name__)

# routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])  #測試
def test():
    a = int(request.form.get('a'))
    b = int(request.form.get('b'))
    c = str(a-b)
    return {'c': c }

@app.route('/api', methods=['POST'])  #當作api
def api():
    latA = float(request.form.get('latA'))
    longA = float(request.form.get('longA'))
    country = str(request.form.get('country'))
    houseType = str(request.form.get('houseType'))
    area = float(request.form.get('area'))
    age = int(request.form.get('age'))
    story = int(request.form.get('story'))
    park = int(request.form.get('park'))
    room = int(request.form.get('room'))
    living = int(request.form.get('living'))
    bath = int(request.form.get('bath'))
    org = int(request.form.get('org'))
    elev = int(request.form.get('elev'))
    internal = [area, age, story, park, room, living, bath, org, elev]
    price = c.getPrice(latA, longA, country, houseType, internal)
    return {'price':str(price[0])}

if __name__ == '__main__':
    app.run()