from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SessionTimeoutModal:

    # Text fields
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, "span.logo")
    PAGE_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".modalDialogBox p")

    # Buttons
    CONTINUE_SESSION_BTN = (By.CSS_SELECTOR, "[id='modalContinueBtn']")
    END_SESSION_BTN = (By.CSS_SELECTOR, "[href='sessionEnded']")


class TimeoutModalHelper(BasePage):

    def click_continue_session_btn(self):
        LOGGER.info("Click on Button: CONTINUE SESSION")
        element = self.find_element(SessionTimeoutModal.CONTINUE_SESSION_BTN)
        self.scrollToElement(element)
        element.click()

    def click_end_session_btn(self):
        LOGGER.info("Click on Button: END SESSION")
        element = self.find_element(SessionTimeoutModal.END_SESSION_BTN)
        self.scrollToElement(element)
        element.click()

    def should_see_session_timeout_modal(self):
        LOGGER.info("Should see Session Timeout Modal")
        try:
            self.find_element(SessionTimeoutModal.PAGE_TITLE_TEXT, time=2)
            self.find_element(SessionTimeoutModal.PAGE_DESCRIPTION_TEXT, time=2)
            self.find_element(SessionTimeoutModal.CONTINUE_SESSION_BTN, time=2)
            self.find_element(SessionTimeoutModal.END_SESSION_BTN, time=2)
            return bool(True)
        except:
            return bool(False)