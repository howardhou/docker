# Python
# refer to : https://docs.docker.com/get-started/part2/

import redis
from flask import Flask
import os
import socket

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def index():
  try:
    visits = redis.incr("counter")
  except:
    visits = "<i>cannot connect to Redis, counter disabled</i>"

  html = "<h3>Hello {name}!</h3>" \
         "<b>Hostname:</b> {hostname}<br/>" \
         "<b>Visits:</b> {visits}"
  return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)