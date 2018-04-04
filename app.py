#holobot
import random
import os
import json
import urllib.request

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

#insults = ['Levine smells like shit', 'Kelsey is just an idea', 'Levine is a pussy vegan bitch','Levine is an adderall filled crack head', 'Levine wishes he was ferda', 'If Levine was my FASET leader I would transfer the instant I heard that faggot\'s voice', 'Levine is a broke boy', 'Levine didn\'t make the middle school basketball team because he is a short jittery fuck', 'Levine is a kike', 'Levine is a blind four eyes weird looking tall grass head having fuck', 'Levine trashes room 1 because he is a disrespectful fuck and doesn\'t deserve to hang with the boys']

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  contents = urllib.request.urlopen("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/get-insult?name=Levine").read()
  #print(contents)
  # We don't want to reply to ourselves!
  if data['text'] == 'RoastLevine':
    msg = contents
    send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : '274e7756a1d2efb25d5d832cb6',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()