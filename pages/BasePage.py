from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LOGGER


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.optoutprescreen.com/"

    def find_element(self, locator, time=10):
        LOGGER.info("Looking for locator with path:\n" + locator[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        LOGGER.info("Looking for locators with path:\n" + locator[1])
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_website(self):
        LOGGER.info("Open URL: " + self.base_url)
        self.driver.get(self.base_url)

    def getDriver(self):
        return self.driver

    def reloadPage(self):
        return self.driver.refresh()

    def scrollToElement(self, element, alignToCenter="true"):
        LOGGER.info("Scroll to Element")
        self.driver.execute_script(
            "arguments[0].scrollIntoView(" + alignToCenter + ");", element)

    def execute_script(self, script, element):
        LOGGER.info("Execute Javascript script:\n" + script)
        self.driver.execute_script(script, element)
