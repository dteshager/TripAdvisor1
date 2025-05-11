#!/usr/bin/env python3
#make a flask hello world app
from flask import Flask, render_template, request, session, redirect, url_for
import os

from api.fetch_data import fetch_tripadvisor_data
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
@app.route('/')
def index():
    session['city'] = request.args.get('city', session.get('city', 'Tacoma'))
    session['state'] = request.args.get('state', session.get('state', 'WA'))
    session['category'] = request.args.get('category', session.get('category', 'restaurants'))

    restaurant_data = fetch_tripadvisor_data(session['city'], session['state'], 'restaurants', use_cache_only=True)
    hotel_data = fetch_tripadvisor_data(session['city'], session['state'], 'hotels', use_cache_only=True)
    attraction_data = fetch_tripadvisor_data(session['city'], session['state'], 'attractions', use_cache_only=True)

    return render_template(
        'index.html',
        city=session['city'],
        state=session['state'],
        category=session['category'],
        restaurant_data=restaurant_data,
        hotel_data=hotel_data,
        attraction_data=attraction_data
    )

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

