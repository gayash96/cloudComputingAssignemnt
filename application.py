import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

application = Flask(__name__)


@application.route('/')
def index():
   print('Request for index page received')
   return render_template('liveScores.html')

@application.route('/liveScores')
def liveScores():
   print('Request for index page received')
   return render_template('liveScores.html')


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
