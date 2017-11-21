from flask import Flask, Blueprint, request, abort
import json
import requests
import config

promote = Blueprint('promote', __name__)


@promote.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        #print("Data received: ")
        #print(request.json)
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_promotionPolicyID = json.dumps(dtr_data["contents"]["promotionPolicyID"])
        contents_digest = json.dumps(dtr_data["contents"]["digest"])
        contents_sourceRepository = json.dumps(dtr_data["contents"]["sourceRepository"])
        contents_sourceTag = json.dumps(dtr_data["contents"]["sourceTag"])
        contents_targetRepository = json.dumps(dtr_data["contents"]["targetRepository"])
        contents_targetTag = json.dumps(dtr_data["contents"]["targetTag"])
        contents_promotedAt = json.dumps(dtr_data["contents"]["promotedAt"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "Promoted image " + contents_sourceRepository + ":" + contents_sourceTag + " to " + contents_targetRepository + " with tag " + contents_targetTag + " at " + contents_promotedAt.strip('"')}
        slack_url=config.refresh()
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
