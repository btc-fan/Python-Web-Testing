import os

# path variables
ROOT_DIR = os.getcwd()
CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/downloaded_captchas/"
FAILED_CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/failed_captchas/"
GENERATED_JSON_FOLDER = ROOT_DIR + "/generated_jsons/"
RESPONSE_JSON = ROOT_DIR + "/generated_jsons/response.json"
UTILS_FOLDER = ROOT_DIR + "/utils/"
DATA_MODEL_FOLDER = ROOT_DIR + "/data_models/"
JSON_DOWNLOAD_BASE64 = GENERATED_JSON_FOLDER + "failed_captchas_base64.json"

# url variables
API_ROOT_URL = "https://lrdcnxcfc3.execute-api.us-west-2.amazonaws.com"
API_RESULTS_URL = API_ROOT_URL + "/result"