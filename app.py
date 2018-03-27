#holobot
import random
import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

insults = ['Levine smells like shit', 'Kelsey is just an idea', 'Levine is a pussy vegan bitch','Levine is an adderall filled crack head', 'Levine wishes he was ferda', 'If Levine was my FASET leader I would transfer the instant I heard that faggot\'s voice']

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # We don't want to reply to ourselves!
  if data['text'] == 'RoastLevine':
    msg = random.choice(insults)
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