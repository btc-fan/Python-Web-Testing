import os

# path variables
ROOT_DIR = os.getcwd()
CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/downloaded_captchas/"
FAILED_CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/failed_captchas/"
UTILS_FOLDER = ROOT_DIR + "/utils/"
DATA_MODEL_FOLDER = UTILS_FOLDER + "/data_models/"
JSON_DOWNLOAD_BASE64 = FAILED_CAPTCHA_DOWNLOAD_FOLDER + "failed_captchas_base64.json"
GENERATED_JSONS = UTILS_FOLDER + "/generated_jsons/response.json"

# url variables
API_ROOT_URL = "https://lrdcnxcfc3.execute-api.us-west-2.amazonaws.com"
API_RESULTS_URL = API_ROOT_URL + "/result"
