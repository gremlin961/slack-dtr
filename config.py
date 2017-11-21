from flask import Flask, render_template, request
import datetime
from tinydb import TinyDB, Query, where
import json

tmpurl = 'https://your.slack.url/token'
db = TinyDB('/database/db.json')
searchdata = Query()

if len(db) == 0:
  db.insert({'id':1, 'slackurl':tmpurl})


def refresh():
    slackdbdata = db.search(searchdata.id == 1)
    slack_url = json.dumps(slackdbdata[0]["slackurl"]).strip('"')
    return slack_url
