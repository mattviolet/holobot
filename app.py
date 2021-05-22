#holobot
import random
import os
import json
import urllib.request

from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from flask import Flask, request
import requests

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

  print("this is the command: " + command)
  print("")
  if ((command == 'roast') and (len(message) > 1)):
    payload = {'name': message[1].lower()}

    #I can probably just set this up on the same mongodb database I used for cooking school?
    #otherwise I might download mongo and try to dockerize it and get it running full time, not sure. Don't I need it to exist (be hosted) somewhere? Will have to see
    ##msg = requests.get("https://nzj7ckgwkf.execute-api.us-east-2.amazonaws.com/Production/get-insult", params=payload)
    roast = "danny lewis is a fraudulent"
    send_message(roast)
  elif ((command == 'addroast') and (len(message)> 2)):
      name = message[1].lower()
      print("This is what is about to be sent to add roast")
      print("")

      payload = {"name" : name, "roast" : roast}
      print(payload)

      #link = urllib.parse.quote("https://ngk7xk5ra5.execute-api.us-east-1.amazonaws.com/prod/add-insult?name=" + name + "&insult=" + roast, safe='/:?=&')
      
      #I think this is the equivalent of doing a post request, not sure though.
      #contents = urllib.request.urlopen(link).read()


  # We don't want to reply to ourselves
  return "ok", 200

def send_message(msg):
  #url  = 'https://api.groupme.com/v3/bots/post'
  url = 'http://localhost:5000/'

  data = { 
          'bot_id' : '2e5e052a7c5b46862969084b43', #I want to use a heroku config variable for this to follow best practices :)
          'text'   : msg,
         }
  print("The data you are about to send to the server")
  print(data)

  ##request = Request(url, urlencode(data).encode())
  ##json = urlopen(request).read().decode()