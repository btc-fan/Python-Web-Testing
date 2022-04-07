from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from utils.logger import LOGGER


class SuccessfulSubmissionPage:
    # Text fields
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, ".confirmation h2.pageTitle")
    GREETING_SUB_HEADING_TITLE_TEXT = (By.CSS_SELECTOR, ".confirmation .pageMarginTop h3")
    SUB_HEADING_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".confirmation .pageMarginTop p:nth-child(3)")
    ENDING_SUB_HEADING_TITLE_TEXT = (By.CSS_SELECTOR, ".confirmation endSession h3")
    ENDING_HEADING_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".confirmation .endSession p")
    INFORMATION_SUMMARY_TITLE_TEXT = (By.CSS_SELECTOR, ".confirmation div.summarySheet h3.subHeading:nth-child(2)")
    NOTE_INFORMATION_SUMMARY_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".confirmation .div.summarySheet p")
    FIELD_NAME_SPAN_TEXT = (By.CSS_SELECTOR, ".confirmation ul.infoWrap div.row span.label")
    FIELD_NAME_VALUE_TEXT = (By.CSS_SELECTOR, ".confirmation ul.infoWrap div.row span.userData")

    # //ul[@class='infoWrap']//div[@class='row']//span[@class='label']
    FIELD_VALUE_TEXT = (By.XPATH, "//ul[@class='infoWrap']//div[@class='row']//span[text()='%s']//..//span[@class='userData']")

    # Buttons
    END_SESSION_BTN = (By.CSS_SELECTOR, "[id='user'] button.primaryBtn")


class SuccessfulSubmissionHelper(BasePage):

    def should_see_successful_submission_page(self):
        LOGGER.info("Should see Successful Submission Page...")
        try:
            self.find_element(SuccessfulSubmissionPage.PAGE_TITLE_TEXT, time=2)
            self.find_element(SuccessfulSubmissionPage.END_SESSION_BTN, time=2)
            self.find_element(SuccessfulSubmissionPage.SUB_HEADING_DESCRIPTION_TEXT, time=2)
            self.find_element(SuccessfulSubmissionPage.ENDING_SUB_HEADING_TITLE_TEXT, time=2)
            self.find_element(SuccessfulSubmissionPage.INFORMATION_SUMMARY_TITLE_TEXT, time=2)
            self.find_element(SuccessfulSubmissionPage.ENDING_HEADING_DESCRIPTION_TEXT, time=2)
            return bool(True)
        except:
            return bool(False)

    def get_successful_submission_field_names(self):
        LOGGER.info("Trying to return Successful Submission User Field Names...")
        filed_names_array = []
        field_names = self.find_elements(SuccessfulSubmissionPage.FIELD_NAME_SPAN_TEXT, time=2)
        for i in field_names:
            filed_names_array.append(i.text)
        return filed_names_array

    def get_successful_submission_field_values(self):
        LOGGER.info("Trying to return Successful Submission User Field Values...")
        filed_values_array = []
        field_values = self.find_elements(SuccessfulSubmissionPage.FIELD_NAME_VALUE_TEXT, time=2)
        for i in field_values:
            filed_values_array.append(i.text)
        return filed_values_array

    def should_have_field_name_equal_to_value(self, field_name, expected_field_value):
        LOGGER.info("Checking if field name: " + field_name.value + "is equal to: " + expected_field_value)
        actual_field_value = self.get_field_value(field_name)
        assert actual_field_value == expected_field_value, LOGGER.error("field name: " + field_name.value + "is NOT equal to: " + expected_field_value)
        return bool(True)

    def get_field_value(self, field_name):
        LOGGER.info("Return field value for: " + field_name.value)
        element = list(SuccessfulSubmissionPage.FIELD_VALUE_TEXT)
        element[1] = element[1].replace("%s", field_name.value)
        element_tuple = tuple(element)
        field_value = self.find_element(element_tuple, time=2)
        return field_value.text
