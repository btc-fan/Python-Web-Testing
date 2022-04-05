import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.BasePage import LOGGER


@pytest.fixture(scope="session", autouse=True)
def browser():
    # BEFORE ALL
    start_time = time.time()
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('disable-notifications')
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    yield driver

    # AFTER ALL
    LOGGER.info("Closing driver")
    driver.close()
    LOGGER.info("Quitting driver")
    driver.quit()
    LOGGER.info("EXECUTION TIME: %.2f seconds", (time.time() - start_time))


def pytest_addoption(parser):
    parser.addoption('--user_json_path', default='', action='store', help='path to user json')
    parser.addoption('--person_data', action='store', default='')


@pytest.fixture()
def user_json_path(request):
    # return request.config.getoption("--user_json_path")
    user_json_path_value = request.config.getoption("--user_json_path")
    if user_json_path_value is None:
        pytest.skip()
    return user_json_path_value

@pytest.fixture()
def person_data(request):
    person_data_value = request.config.getoption("--person_data")
    return person_data_value

# @fixture()
# def user_json_path(request):
#     return request.config.getoption("--user_json_path")

#
#
# def pytest_generate_tests(metafunc):
#     option_value = metafunc.config.option.user_json_path
#     if 'user_json_path' in metafunc.fixturenames and option_value is not None:
#         metafunc.parametrize("user_json_path", [option_value])
