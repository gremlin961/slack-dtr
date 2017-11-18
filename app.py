from flask import Flask, request, abort
import json
import requests
import os

app = Flask(__name__)
slack_url = os.environ['slack_url']

@app.route('/push', methods=['POST'])
def push():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
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
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
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
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/manpush', methods=['POST'])
def manpush():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
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

        slack_data = {"text": "User " + contents_author.strip('"') + " pushed manifest " + contents_imageName + " at " + contents_pushedAt.strip('"') + ". View more info here: <https://dtr.richard.dtcntr.net/repositories/" + contents_namespace.strip('"') + "/" + contents_repository.strip('"') + "/tags>"}
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/mandelete', methods=['POST'])
def mandelete():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
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

        slack_data = {"text": "User " + contents_author.strip('"') + " deleted manifest " + contents_imageName + " at " + contents_deletedAt.strip('"')}
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/scan', methods=['POST'])
def scan():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
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
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/scanfail', methods=['POST'])
def scanfail():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_namespace = json.dumps(dtr_data["contents"]["namespace"])
        contents_repository = json.dumps(dtr_data["contents"]["repository"])
        contents_tag = json.dumps(dtr_data["contents"]["tag"])
        contents_imageName =  json.dumps(dtr_data["contents"]["imageName"])
        event_location = json.dumps(dtr_data["location"])
        slack_data = {"text": "Image scan failed for " + contents_imageName + " at " + summary_checkcompletedat.strip('"')}
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

@app.route('/promote', methods=['POST'])
def promote():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
        dtr_data = request.json
        event_type = json.dumps(dtr_data["type"])
        event_createdAt = json.dumps(dtr_data["createdAt"])
        contents_promotionPolicyID = json.dumps(dtr_data["contents"]["promotionPolicyID"])
        contents_digest = json.dumps(dtr_data["contents"]["digest"])
        contents_sourceRepository = json.dumps(dtr_data["contents"]["sourceRepository"])
        contents_sourceTag = json.dumps(dtr_data["contents"]["sourceTag"])
        contents_targetRepository = json.dumps(dtr_data["contents"]["targetRepository"])
        contents_targetTag = json.dumps(dtr_data["contents"]["targetTag"])
        contents_promotedAt = json.dumps(dtr_data["contents"]["pushedAt"])
        event_location = json.dumps(dtr_data["location"])

        slack_data = {"text": "Promoted image + " contents_sourceRepository + ":" + contents_sourceTag + " to " + contents_targetRepository + " with tag " + contents_targetTag + " at " + contents_promotedAt.strip('"')}
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
