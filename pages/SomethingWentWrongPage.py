from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SomethingWentWrongPage:

    # Text fields
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, "")


class SomethingWentWrongHelper(BasePage):

    def should_see_something_went_wrong_page(self):
        LOGGER.info("Should see Something Went Wrong Page")
        try:
            self.find_element(SomethingWentWrongPage.PAGE_TITLE_TEXT, time=2)
            return bool(True)
        except:
            return bool(False)