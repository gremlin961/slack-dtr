from flask import Flask, Blueprint, request, abort
import json
import requests
import config

push = Blueprint('push', __name__)


@push.route('', methods=['GET', 'POST'])
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
        contents_pushedAt = json.dumps(dtr_data["contents"]["pushedAt"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "User " + contents_author.strip('"') + " pushed tag " + contents_imageName + " at " + contents_pushedAt.strip('"') + ". View more info here: <https://dtr.richard.dtcntr.net/repositories/" + contents_namespace.strip('"') + "/" + contents_repository.strip('"') + "/tags>"}
        slack_url=config.refresh()
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    if request.method == 'GET':
        return "working"
    #else:
        #abort(400)