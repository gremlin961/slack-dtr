from flask import Flask, request, abort
import json
import requests

app = Flask(__name__)
slack_url = os.environ['slack_url']

@app.route('/push', methods=['POST'])
def push():
    if request.method == 'POST':
        print("Data received: ")
        print(request.json)
        dtr_data = request.json
        dtr_image = json.dumps(dtr_data["contents"]["imageName"])
        dtr_user = json.dumps(dtr_data["contents"]["author"])
        dtr_namespace = json.dumps(dtr_data["contents"]["namespace"])
        dtr_repo = json.dumps(dtr_data["contents"]["repository"])
        dtr_time = json.dumps(dtr_data["contents"]["pushedAt"])
        slack_data = {"text": "User " + dtr_user.strip('"') + " pushed tag " + dtr_image + " at " + dtr_time.strip('"') + ". View more info here: <https://dtr.richard.dtcntr.net/repositories/" + dtr_namespace.strip('"') + "/" + dtr_repo.strip('"') + "/tags>"}
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
        dtr_image = json.dumps(dtr_data["contents"]["imageName"])
        scan_critical = json.dumps(dtr_data["contents"]["scanSummary"]["critical"])
        dtr_time = json.dumps(dtr_data["contents"]["scanSummary"]["check_completed_at"])
        slack_data = {"text": "Image scan completed for " + dtr_image + " at " + dtr_time.strip('"') + " with "+ scan_critical + " critical warnings."}
        response = requests.post(slack_url, data=json.dumps(slack_data),headers={'Content-Type': 'application/json'})
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
