import os

# path variables
ROOT_DIR = os.getcwd()
CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/downloaded_captchas/"
FAILED_CAPTCHA_DOWNLOAD_FOLDER = ROOT_DIR + "/failed_captchas/"
UTILS_FOLDER = ROOT_DIR + "/utils/"
DATA_MODEL_FOLDER = UTILS_FOLDER + "/data_models/"
JSON_DOWNLOAD_BASE64 = FAILED_CAPTCHA_DOWNLOAD_FOLDER + "failed_captchas_base64.json"
