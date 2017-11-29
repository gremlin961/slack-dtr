# Configuration module used to create and modify the TinyDB instance used track the Slack Application URL

#from flask import Flask, render_template, request
#import datetime
from tinydb import TinyDB, Query, where
import json

# Set the default URL that will be displayed in the dtrwebhook main endpoint. This will be replaced by the user when configuring the Slack Applicaiton URL
tmpurl = 'https://your.slack.url/token'

# Define the location of the db.json file used by TinyDB. Recommendation is to create a persistent volume and mount it to "/database"
db = TinyDB('/database/db.json')
searchdata = Query()

# Initialize the database with tmpurl if it does not already exist
if len(db) == 0:
  db.insert({'id':1, 'slackurl':tmpurl})

# Primary function used to pull the value of the Slack Applicaiton URL from the database and return it as "slack_url"
def refresh():
    slackdbdata = db.search(searchdata.id == 1)
    slack_url = json.dumps(slackdbdata[0]["slackurl"]).strip('"')
    return slack_url
