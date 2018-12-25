#holobot
import random
import os
import json
import urllib.request


from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

#insults = ['Levine smells like shit', 'Kelsey is just an idea', 'Levine is a pussy vegan bitch','Levine is an adderall filled crack head', 'Levine wishes he was ferda', 'If Levine was my FASET leader I would transfer the instant I heard that faggot\'s voice', 'Levine is a broke boy', 'Levine didn\'t make the middle school basketball team because he is a short jittery fuck', 'Levine is a kike', 'Levine is a blind four eyes weird looking tall grass head having fuck', 'Levine trashes room 1 because he is a disrespectful fuck and doesn\'t deserve to hang with the boys']

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  # if (data['text'] == 'add'):
  #   print('reached here')
  #   string = "appendtest space"
  #   ##learn how to escape just spaces
  #   link = urllib.parse.quote("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/add-insult?name=matt&insult=" + string, safe='/:?=&')
  #   contents = urllib.request.urlopen(link).read()


  ## either [roast, name] or [addRoast, name, insult]
  message = data['text'].split(' ')
  ## either roast or addRoast
  command = message[0].lower()

  if (len(message) > 2):
    roast = " ".join(message[2:]).replace(u"\2019", "'")

  print(command)
  if ((command == 'roast') and (len(message) > 1)):
    msg = urllib.request.urlopen("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/get-insult?name=" + message[1].lower()).read()
    send_message(msg)
  elif ((command == 'addroast') and (len(message)> 2)):
      name = message[1].lower()
      #print(name)
      #print(roast)
      link = urllib.parse.quote("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/add-insult?name=" + name + "&insult=" + roast, safe='/:?=&')
      print(link)
      contents = urllib.request.urlopen(link).read()


  # We don't want to reply to ourselves
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : '274e7756a1d2efb25d5d832cb6',
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()