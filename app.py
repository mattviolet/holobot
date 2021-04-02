#holobot
import random
import os
import json
import urllib.request

from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from flask import Flask, request
##import requests

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()

  ## either [roast, name] or [addRoast, name, insult]
  message = data['text'].split(' ')
  ## either roast or addRoast
  command = message[0].lower()

  if (len(message) > 2):
    roast = " ".join(message[2:]).replace(u"\2019", "'")

  print(command)
  if ((command == 'roast') and (len(message) > 1)):
    payload = {'name': message[1].lower()}
    msg = requests.get("https://nzj7ckgwkf.execute-api.us-east-2.amazonaws.com/Production/get-insult")
    print(msg)
    #send_message(msg)
  #elif ((command == 'addroast') and (len(message)> 2)):
      #name = message[1].lower()
      #print(name)
      #print(roast)
      #link = urllib.parse.quote("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/add-insult?name=" + name + "&insult=" + roast, safe='/:?=&')
      #print(link)
      #contents = urllib.request.urlopen(link).read()


  # We don't want to reply to ourselves
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = { 
          'bot_id' : '2e5e052a7c5b46862969084b43', #I want to use a heroku config variable for this to follow best practices :)
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()