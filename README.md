# holobot
Groupme bot made using python used to roast people in groupme

Welcome to holobot!

To run, clone the repo and run the following commands in your termial.

1. export FLASK_APP=app.py -this designates which file to execute when we run 'flask run'

2. flask run - this starts running a flask server on a local port

3. Change the bot id to your bot and then you can start sending POST request with cURL in your terminal. (I use the terminal within VSCode) 

Example: "curl --header content-Type: application/json" -d "{\"text\":\"roast Violet\"}" http:/localhost:5000/"

This will send a POST request with the contents: {"text" : "roast Violet"} to port 5000
which should trigger holobot if everything else is set up correctly.

