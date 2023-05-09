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

@application.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@application.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   application.run()
