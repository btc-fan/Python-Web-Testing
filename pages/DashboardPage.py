from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from utils.logger import LOGGER


class DashboardPage:
    CLICK_HERE_BTN = (By.CSS_SELECTOR, "[id='home'] button.primaryBtn")


class DashboardHelper(BasePage):

    def click_here_btn(self):
        LOGGER.info("Click on Button: Click Here to Opt-In or Opt-Out")
        element = self.find_element(DashboardPage.CLICK_HERE_BTN)
        self.scrollToElement(element)
        element.click()
