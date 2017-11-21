from flask import Flask, Blueprint, request, abort
import json
import requests
import config

scanfail = Blueprint('scanfail', __name__)


@scanfail.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_tag = json.dumps(dtr_data["contents"]["tag"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "Image scan failed for " + contents_imageName}
        slack_url=config.refresh()
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
