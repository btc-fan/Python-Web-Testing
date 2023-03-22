from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SessionEndedPage:
    PAGE_TITLE = (By.CSS_SELECTOR, ".sessionEnded h2.pageTitle")
    SUB_HEADING = (By.CSS_SELECTOR, ".sessionEnded h3.subHeading")
    PAGE_DESCRIPTION = (By.CSS_SELECTOR, ".sessionEnded div.pageMarginTop p")


class SessionEndedHelper(BasePage):

    def should_see_session_ended_page(self):
        LOGGER.info("Should see Session Ended Page")
        try:
            self.find_element(SessionEndedPage.PAGE_TITLE, time=2)
            self.find_element(SessionEndedPage.SUB_HEADING, time=2)
            self.find_element(SessionEndedPage.PAGE_DESCRIPTION, time=2)
            return bool(True)
        except:
            return bool(False)