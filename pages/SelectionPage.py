from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SelectionPage:
    OPT_IN_RADIO_BTN = (By.CSS_SELECTOR, "li [id='formChoice1']")
    ELECTRONIC_OPT_OUT_RADIO_BTN = (By.CSS_SELECTOR, "li [id='formChoice2']")
    PERMANENT_OPT_OUT_RADIO_BTN = (By.CSS_SELECTOR, "li [id='formChoice3']")
    CONTINUE_HERE_BTN = (By.CSS_SELECTOR, "div.selectOptionTypeForm .primaryBtn")


class SelectionHelper(BasePage):

    def click_opt_in_radio_btn(self):
        LOGGER.info("Click on Radio Button: Opt-In")
        element = self.find_element(SelectionPage.OPT_IN_RADIO_BTN)
        self.scrollToElement(element)
        element.click()

    def click_electronic_opt_out_radio_btn(self):
        LOGGER.info("Click on Radio Button: Electronic Opt-Out for 5 years")
        element = self.find_element(SelectionPage.ELECTRONIC_OPT_OUT_RADIO_BTN)
        self.scrollToElement(element)
        element.click()

    def click_permanent_opt_out_radio_btn(self):
        LOGGER.info("Click on Radio Button: Permanent Opt-Out by Mail")
        element = self.find_element(SelectionPage.PERMANENT_OPT_OUT_RADIO_BTN)
        self.scrollToElement(element)
        element.click()

    def click_continue_btn(self):
        LOGGER.info("Click on Button: Continue")
        element = self.find_element(SelectionPage.CONTINUE_HERE_BTN)
        self.scrollToElement(element)
        element.click()
