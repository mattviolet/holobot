#holobot
import random
import os
import json
import urllib.request
import pymongo

from pprint import pprint
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

from flask import Flask, request
import requests

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://mviolet:Mlab4016449821@holotbot.stvmv.mongodb.net/holobot?retryWrites=true&w=majority")
db = client["holobot"]
names = db["names"]

@app.route('/', methods=['POST'])
def webhook():
  print("")
  data = request.get_json()
  print(data)
  ## either [roast, name] or [addRoast, name, insult]
  message = data['text'].split(' ')
  name = message[1]
  ## either roast or addRoast
  command = message[0].lower()
  target = names.find_one({"name" : name })
  print(target)


  print("this is the message: " + data['text'])
  print("")
  if ((command == 'roast') and (len(message) > 1)): 
    roast = random.choice(target['insults'])
    send_roast(roast)
  elif ((command == 'addroast') and (len(message)> 2)):
      ##get the name and roast
      roast = " ".join(message[2:]).replace(u"\2019", "'")

      #get the current list of roasts for this person
      current_insults = target['insults']
      #add the new roast
      current_insults.append(roast)
      new_insults = current_insults

      #update the list in the db to the new list with the new roast
      names.update_one({"_id" : target["_id"]},
      {'$set':
        { 'insults' : new_insults }  
      })

      for target in names.find():
        print("new object: ")
        print(target)

  # We don't want to reply to ourselves
  return "ok", 200

def send_roast(roast):
  groupme  = 'https://api.groupme.com/v3/bots/post'
  #url = 'http://localhost:5000/'

  payload = { 
          'bot_id' : '2e5e052a7c5b46862969084b43', #I want to use a heroku config variable for this to follow best practices :)
          'text'   : roast,
         }

  print("The data you are about to send to the server")
  print(payload)

  reqString = json.dumps(payload)
  request = requests.post(groupme, data = reqString)

