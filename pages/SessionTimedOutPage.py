from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SessionTimedOutPage:

    # Text fields
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, "h2.pageTitle")
    SUB_HEADING_TEXT = (By.CSS_SELECTOR, "h3.subHeading")
    PAGE_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".pageMarginTop p")

    # Buttons
    RETURN_TO_HOMEPAGE_BTN = (By.CSS_SELECTOR, ".sessionExpiredReturn")


class SessionTimedOutHelper(BasePage):

    def should_see_session_timed_out_page(self):
        LOGGER.info("Should see Session Timed Out Page")
        try:
            self.find_element(SessionTimedOutPage.PAGE_TITLE_TEXT, time=2)
            self.find_element(SessionTimedOutPage.SUB_HEADING_TEXT, time=2)
            self.find_element(SessionTimedOutPage.PAGE_DESCRIPTION_TEXT, time=2)
            self.find_element(SessionTimedOutPage.RETURN_TO_HOMEPAGE_BTN, time=2)
            return bool(True)
        except:
            return bool(False)