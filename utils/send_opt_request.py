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

# returns a json formatted payload for submission


def get_payload():
    request_payload = {
        "UUID": "<%- || null %>",
        "submitSuccess": "<%- || false %>",
        "attemptAt": "<%- || null %>",
        "completedAt": "<%- || null %>",
        "attempts": "<%- || 0 %>",
        "logs": "<%- || null %>",
        "captcha": [
            {
                "success": "<%- || true %>",
                "img": "<%- 'base64 encoded image' || null %>"
            }
        ],
        "responseMessage": "<%- 'string' || null %>",
        "errors": []
    }
    return request_payload

# form request to POST


def send_request():
    requestPayload = get_payload()
    data = json.dumps(requestPayload)
    r = requests.post(variables.API_RESULTS_URL, auth=(
        authUser, authPass), json=data)
    print(r.status_code)
    print(r.text)


def main():
    check_connection()
    send_request()


if __name__ == '__main__':
    sys.exit(main())
