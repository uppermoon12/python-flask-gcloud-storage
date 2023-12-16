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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))