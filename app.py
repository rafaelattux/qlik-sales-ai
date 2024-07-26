from flask import (Flask)

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/')
def index():
   print('Request for index page received')
   return app.send_static_file('index.html')


if __name__ == '__main__':
   app.run(threaded=True, port=8000)