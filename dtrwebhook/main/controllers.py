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
        slack_url=config.refresh()
        return render_template('index.html', date_time=datetime.datetime.now(), slack_url=slack_url)
    if request.method == 'GET':
        slack_url=config.refresh()
        return render_template('index.html', date_time=datetime.datetime.now(), slack_url=slack_url)
