import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import json
import urllib.request
import certifi

application = Flask(__name__)


@application.route('/liveScores')
def liveScores():
   response = urllib.request.urlopen("https://api.cricapi.com/v1/currentMatches?apikey=9eb76118-7292-43f8-93eb-6f0ab8f19bf2&offset=0", cafile=certifi.where())
   matches = []
   matchData = json.loads(response.read().decode())['data']
   for match in matchData:
      matches.append({
         'name': match['name'],
         'status': match['status'],
         'venue': match['venue'],
         'date': match['date'],
         'score': match['score']
      })
   print(matches)
   return render_template('liveScores.html', matches=matches)

@application.route('/scoreBoard')
def scoreBoard():
   response = urllib.request.urlopen("https://api.cricapi.com/v1/cricScore?apikey=9eb76118-7292-43f8-93eb-6f0ab8f19bf2", cafile=certifi.where())
   matches = []
   matchData = json.loads(response.read().decode())['data']
   for match in matchData:
      matches.append({
         'name': match['t1'] + ' vs '+ match['t2'],
         'status': match['status'],
         'score': match['t1'] + ' : ' + match['t1s']+ ' ' +match['t2'] + ' : ' + match['t2s'],
         'date': match['dateTimeGMT'],
         'matchType': match['matchType'],
         'ms': match['ms']
      })
   print(matches)
   return render_template('scoreBoard.html', matches=matches)

@application.route('/upcomingMatches')
def upcomingMatches():
   response = urllib.request.urlopen("https://api.cricapi.com/v1/cricScore?apikey=9eb76118-7292-43f8-93eb-6f0ab8f19bf2", cafile=certifi.where())
   matches = []
   matchData = json.loads(response.read().decode())['data']
   for match in matchData:
      matches.append({
         'name': match['t1'] + ' vs '+ match['t2'],
         'status': match['status'],
         'score': match['t1'] + ' : ' + match['t1s']+ ' ' +match['t2'] + ' : ' + match['t2s'],
         'date': match['dateTimeGMT'],
         'matchType': match['matchType'],
         'ms': match['ms']
      })
   print(matches)
   return render_template('upcomingMatches.html', matches=matches)

@application.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@application.route('/liveScores/venue_weather/<venue>')
def weather(venue):
   city = str(venue)
   url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=080acdfd2e43c709c852fa5073c6b36d'
   response = urllib.request.urlopen(url, cafile=certifi.where())
   data = json.loads(response.read().decode())
   location = data['name']
   temperature = data['main']['temp']
   weather = data['weather'][0]['description']
   weather_icon = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"

   forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid=080acdfd2e43c709c852fa5073c6b36d'
   forecast_response = urllib.request.urlopen(forecast_url, cafile=certifi.where())
   forecast_data = json.loads(forecast_response.read().decode())
   forecast_list = forecast_data['list']
   forecast_data = []
   for forecast in forecast_list:
        forecast_time = forecast['dt_txt']
        temperature = forecast['main']['temp']
        weather_description = forecast['weather'][0]['description']
        forecast_data.append({
            'time': forecast_time,
            'temperature': temperature,
            'description': weather_description
        })


   return render_template('weather.html', location=location, temperature=temperature, weather=weather, weather_icon=weather_icon, forecast_data=forecast_data)

if __name__ == '__main__':
   application.run()
