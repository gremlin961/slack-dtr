from flask import Flask, Blueprint, render_template, request
from tinydb import TinyDB, Query, where
import json
import datetime
import config


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        urlupdate=request.form['slack_url']
        config.db.update({'slackurl':urlupdate}, where('id') == 1)
        #slackdbdata = config.db.search(config.searchdata.id == 1)
        #slack_url = json.dumps(slackdbdata[0]["slackurl"]).strip('"')
        slack_url=config.refresh()
        return render_template('index.html', date_time=datetime.datetime.now(), slack_url=slack_url)
    if request.method == 'GET':
        #slackdbdata = config.db.search(config.searchdata.id == 1)
        # = json.dumps(slackdbdata[0]["slackurl"]).strip('"')
        slack_url=config.refresh()
        return render_template('index.html', date_time=datetime.datetime.now(), slack_url=slack_url)
