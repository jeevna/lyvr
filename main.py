import os
from flask import Flask, request, redirect, session, render_template
from datetime import timedelta
import sys

# =========== gcloud initialization =================
import base64
import json
import os

from google.cloud import pubsub_v1
from google.cloud import storage
from google.cloud import translate
from google.cloud import vision

vision_client = vision.ImageAnnotatorClient()
translate_client = translate.Client()
publisher = pubsub_v1.PublisherClient()
storage_client = storage.Client()

project_id = os.environ['GCP_PROJECT']

with open('config.json') as f:
    data = f.read()
config = json.loads(data)

# =========== gcloud initialization =================


app = Flask(__name__)
#app.debug = True

# ------------------++++ INITIALIZE application ++++---------------------------------#

sys.path.insert(0, '')

import pages
app.register_blueprint(pages.bp)


# ------------------- ERRORS -----------------------------#
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errorpage.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errorpage.html'), 500

@app.errorhandler(403)
def page_forbidden(error):
    return render_template('errorpage.html'), 500


if __name__ == '__main__':
    app.run()
