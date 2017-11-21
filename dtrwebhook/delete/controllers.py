from flask import Flask, Blueprint, request, abort
import json
import requests
import config

delete = Blueprint('delete', __name__)


@delete.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        #print("Data received: ")
        #print(request.json)
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_tag = json.dumps(dtr_data["contents"]["tag"])
        contents_digest = json.dumps(dtr_data["contents"]["digest"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        contents_os = json.dumps(dtr_data["contents"]["os"])
        contents_architecture = json.dumps(dtr_data["contents"]["architecture"])
        contents_author = json.dumps(dtr_data["contents"]["author"])
        contents_deletedAt = json.dumps(dtr_data["contents"]["deletedAt"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "User " + contents_author.strip('"') + " deleted tag " + contents_imageName + " at " + contents_deletedAt.strip('"')}
        slack_url=config.refresh()
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
