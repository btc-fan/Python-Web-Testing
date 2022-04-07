import json
import sys
import requests
import credentials as creds
import variables

authUser = creds.basicAuthUser
authPass = creds.basicAuthPassword

# verify the user action is authorized, should return 200 status
def check_connection():
    r = requests.get(variables.API_ROOT_URL, auth=(authUser, authPass))
    print(r.status_code)
    print(r.text)

# returns a json formatted payload for POST operation
def prepare_payload():
    response_file = variables.GENERATED_JSONS
    with open(response_file, 'r') as responseFile:
        data = json.load(responseFile)
        for obj in data:
            send_request(obj)

# POST request 
def send_request(data):
    r = requests.post(variables.API_RESULTS_URL, auth=(
        authUser, authPass), json=data)
    print(r.status_code)
    print(r.text)

def main():
    check_connection()
    prepare_payload()

if __name__ == '__main__':
    sys.exit(main())
