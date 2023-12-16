from flask import Flask, request, jsonify
import os
import sys
from google.cloud import storage
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
import json

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World!"

@app.route('/connect', methods=['GET'])
def connect():
    service_account = json.loads(os.environ.get("GOOGLE_CLOUD_CREDENTIALS"))
    creds = Credentials.from_service_account_info(service_account)
    client = storage.Client(credentials=creds)
    bucket = client.bucket('skillshift-bucket')

    base_images_dir = 'photos/freelancers/freelancer_blabla123ganteng/base_images/'
    base_images = bucket.blob(base_images_dir)
    return jsonify({"message": base_images})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))