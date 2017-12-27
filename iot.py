import RPi.GPIO as GPIO
import json
import os

from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(16, GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
GPIO.setup(18, GPIO.OUT)   ## Setup GPIO Pin to OUTPUT

@app.route('/',methods=['POST'])
def index():
    req = request.get_json(silent=True, force=True)
    val = processRequest(req)
    #print(val)
    r = make_response(json.dumps(val))
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    
    device = req['device']
    state = json.loads(req['state'])
    #print(state)
    if device=='demo light':
        GPIO.output(16, state) ## State is true/false
    elif device=='bedroom fan':
        GPIO.output(18, state) ## State is true/false
        
    return {
    "speech": "it is done",
    "displayText": "it is done",
    # "data": data,
    # "contextOut": [],
    "source": "apiai-weather-webhook-sample"
    }

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)


