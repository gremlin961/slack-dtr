from flask import Flask, Blueprint, request, abort
import json
import requests
import config

scan = Blueprint('scan', __name__)


@scan.route('', methods=['POST'])
def index():
    if request.method == 'POST':
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_tag = json.dumps(dtr_data["contents"]["tag"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        summary_namespace = json.dumps(dtr_data["contents"]["scanSummary"]["namespace"])
        summary_reponame = json.dumps(dtr_data["contents"]["scanSummary"]["reponame"])
        summary_tag = json.dumps(dtr_data["contents"]["scanSummary"]["tag"])
        summary_critical = json.dumps(dtr_data["contents"]["scanSummary"]["critical"])
        summary_major = json.dumps(dtr_data["contents"]["scanSummary"]["major"])
        summary_minor = json.dumps(dtr_data["contents"]["scanSummary"]["minor"])
        summary_lastscanstatus = json.dumps(dtr_data["contents"]["scanSummary"]["last_scan_status"])
        summary_checkcompletedat = json.dumps(dtr_data["contents"]["scanSummary"]["check_completed_at"])
        summary_shouldrescan = json.dumps(dtr_data["contents"]["scanSummary"]["should_rescan"])
        summary_hasforeignlayers = json.dumps(dtr_data["contents"]["scanSummary"]["has_foreign_layers"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "Image scan completed for " + contents_imageName + " at " + summary_checkcompletedat.strip('"') + " with "+ summary_critical + " critical warnings, " + summary_major + " major warnings, and " + summary_minor + " minor warnings."}
        slack_url=config.refresh()
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)
