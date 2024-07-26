import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/oauth_callback.html')
def index():
   print('Request for oauth_callback page received')
   return render_template('oauth_callback.html')


if __name__ == '__main__':
   app.run()