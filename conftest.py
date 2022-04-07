import json

import pytest
import time
import zulu

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.BasePage import LOGGER
from utils.variables import RESPONSE_JSON


@pytest.fixture(scope="function", autouse=True)
def browser():

    # BEFORE ALL
    pytest.captcha_response_array.clear()
    attempted_at = zulu.now()
    start_time = time.time()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    yield driver
    # AFTER ALL
    LOGGER.info("Closing driver")
    driver.close()
    LOGGER.info("Quitting driver")
    driver.quit()
    end_time = time.time()
    duration = (start_time - end_time)
    LOGGER.info("EXECUTION TIME: %.2f seconds", duration)

    completed_at = zulu.now()

    pytest.response_data_object['attemptAt'] = str(attempted_at)
    pytest.response_data_object['completedAt'] = str(completed_at)

    try:
        with open(RESPONSE_JSON, "r+") as f:
            file_data = json.load(f)
            file_data.append(pytest.response_data_object)
            f.seek(0)
            json.dump(file_data, f, indent=4, separators=(',', ': '))
            f.close()
    except FileNotFoundError:
        pytest.response_data_array.append(pytest.response_data_object)
        response_data_json = json.loads(json.dumps(pytest.response_data_array))
        with open(RESPONSE_JSON, "a+") as f:
            json.dump(response_data_json, f, indent=4, separators=(',', ': '))
            f.close()

def pytest_configure():
    pytest.response_data_array = []
    pytest.response_data_object = {}
    pytest.captcha_response_array = []
    pytest.captcha_response_object = {}
    pytest.errors_response_array = []
    pytest.errors_response_object = {}
    pytest.captcha_response_array.clear()

    pytest.response_data_object['UUID'] = None
    pytest.response_data_object['submitSuccess'] = None
    pytest.response_data_object['attemptAt'] = None
    pytest.response_data_object['completedAt'] = None
    pytest.response_data_object['attempts'] = None
    pytest.response_data_object['captcha'] = None
    pytest.response_data_object['responseMessage'] = None
    pytest.response_data_object['errors'] = None

def pytest_addoption(parser):
    parser.addoption('--user_json_path', default='', action='store', help='path to user json')
    parser.addoption('--person_data', action='store', default='')


@pytest.fixture()
def user_json_path(request):
    user_json_path_value = request.config.getoption("--user_json_path")
    if user_json_path_value is None:
        pytest.skip()
    return user_json_path_value

@pytest.fixture()
def person_data(request):
    person_data_value = request.config.getoption("--person_data")
    return person_data_value

