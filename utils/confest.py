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
