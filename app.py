from flask import Flask, request, abort
import json
import requests
import os

app = Flask(__name__)
slack_url = os.environ['slack_url']

@app.route('/webhook', methods=['POST'])
def webhook():
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


if __name__ == '__main__':
    app.run()
