import json
import sys

import requests

import utils.credentials as creds
from utils.logger import LOGGER
from utils.variables import *

authUser = creds.basicAuthUser
authPass = creds.basicAuthPassword

# verify the user action is authorized, should return 200 status
def check_connection():
    LOGGER.info("Checking API connection for endpoint\n" + API_ROOT_URL)
    r = requests.get(API_ROOT_URL, auth=(authUser, authPass))
    LOGGER.info(r.status_code)
    LOGGER.info(r.text)

# returns a json formatted payload for POST operation
def prepare_payload():
    LOGGER.info("Preparing Response Json from path:\n" + RESPONSE_JSON)
    response_file = RESPONSE_JSON
    with open(response_file, 'r') as responseFile:
        data = json.load(responseFile)
        for obj in data:
            send_request(obj)

# POST request 
def send_request(data):
    LOGGER.info("Sending Reqesuest with data:\n" + str(data))
    r = requests.post(API_RESULTS_URL, auth=(
        authUser, authPass), json=data)
    LOGGER.info(r.status_code)
    LOGGER.info(r.text)

def main_api():
    check_connection()
    prepare_payload()
    LOGGER.info("Response Json file SUCCESSFULLY send to API")

if __name__ == '__main__':
    sys.exit(main_api())
