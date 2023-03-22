from selenium.webdriver.common.by import By

from pages.BasePage import BasePage

# from utils.utils import retry
from utils.logger import LOGGER


class OptInOptOutForm:

    # Text fields
    PAGE_TITLE_TEXT = (By.CSS_SELECTOR, "h2.pageTitle")
    SUB_HEADING_TITLE_TEXT = (By.CSS_SELECTOR, "h3.subHeading")
    SUB_HEADING_DESCRIPTION_TEXT = (By.CSS_SELECTOR, "div.pageMarginTop div")
    CAPTCHA_DESCRIPTION_TEXT = (By.CSS_SELECTOR, "div.captchaBox label")
    CAPTCHA_CONFIRM_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".confirmWrap p.buttonMessaging")
    CAPTCHA_CANCEL_DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".cancelWrap p.buttonMessaging")

    # Input fields
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[id='opt_fname']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[id='opt_lname']")
    SSN1_INPUT = (By.CSS_SELECTOR, "[id='ssn_1']")
    SSN2_INPUT = (By.CSS_SELECTOR, "[id='ssn_2']")
    SSN3_INPUT = (By.CSS_SELECTOR, "[id='ssn_3']")
    STREET_ADDRESS_INPUT = (By.CSS_SELECTOR, "[id='opt_street']")
    CITY_INPUT = (By.CSS_SELECTOR, "[id='cityInput'] input")
    ZIP_INPUT = (By.CSS_SELECTOR, "[id='opt_zip']")
    CAPTCHA_IMG = (By.CSS_SELECTOR, "div.captchaBox img")
    CAPTCHA_ANSWER_INPUT = (By.CSS_SELECTOR, "[id='captchaAnswer']")
    MIDDLE_NAME_INPUT = (By.CSS_SELECTOR, "[id='opt_mname']")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "[id='datepicker']")
    APT_SUITE_INPUT = (By.CSS_SELECTOR, "[id='opt_apt']")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "[id='phone']")

    # Error fields
    CAPTCHA_ERROR_TXT = (By.CSS_SELECTOR, "[id='captcha.errors']")

    # Dropdown
    STATE_DROPDOWN_VALUE = (By.CSS_SELECTOR, "[id='opt_state']")
    STATE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "[id='opt_state'] option")

    SUFFIX_DROPDOWN_VALUE = (By.CSS_SELECTOR, "[id='suffix']")
    SUFFIX_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "[id='suffix'] option")

    # Buttons
    CONFIRM_BTN = (By.CSS_SELECTOR, ".confirmCancelWrap button")
    CANCEL_BTN = (By.CSS_SELECTOR, ".cancelWrap button")


class BasicInfoHelper(BasePage):

    def enter_first_name(self, value):
        LOGGER.info("Enter FIRST NAME value: " + value)
        element = self.find_element(OptInOptOutForm.FIRST_NAME_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have FIRST NAME Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.FIRST_NAME_INPUT).get_attribute('value')
        #TODO add retry methods here. Three times at least
        assert input_text == value, LOGGER.error('FIRST NAME value is not inserted properly')

    def enter_last_name(self, value):
        LOGGER.info("Enter LAST NAME value: " + value)
        element = self.find_element(OptInOptOutForm.LAST_NAME_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have LAST NAME Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.LAST_NAME_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('LAST NAME value is not inserted properly')

    def enter_city(self, value):
        LOGGER.info("Enter CITY name value: " + value)
        element = self.find_element(OptInOptOutForm.CITY_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have CITY Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.CITY_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('CITY value is not inserted properly')

    def enter_full_ssn(self, value):
        LOGGER.info("Enter full SSN value: " + value)
        self.enter_ssn1(value[0:3])
        self.enter_ssn2(value[3:5])
        self.enter_ssn3(value[5:9])

    def enter_ssn1(self, value):
        LOGGER.info("Enter ssn1 value: " + value)
        element = self.find_element(OptInOptOutForm.SSN1_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have ssn1 Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.SSN1_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('ssn1 value is not inserted properly')

    def enter_ssn2(self, value):
        LOGGER.info("Enter ssn2 value: " + value)
        element = self.find_element(OptInOptOutForm.SSN2_INPUT)
        element.send_keys(value)
        # retry(self.find_element(BasicInfoPage.SSN2_INPUT).get_attribute('value') == value, 3, 0.3, 15)
        LOGGER.info("Should have ssn2 Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.SSN2_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('ssn2 value is not inserted properly')

    def enter_ssn3(self, value):
        LOGGER.info("Enter ssn3 value: " + value)
        element = self.find_element(OptInOptOutForm.SSN3_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have ssn3 Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.SSN3_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('ssn3 value is not inserted properly')

    def enter_street_address(self, value):
        LOGGER.info("Enter STREET ADDRESS value: " + value)
        element = self.find_element(OptInOptOutForm.STREET_ADDRESS_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have STREET ADDRESS Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.STREET_ADDRESS_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('STREET ADDRESS value is not inserted properly')

    def enter_zip(self, value):
        LOGGER.info("Enter ZIP value: " + value)
        element = self.find_element(OptInOptOutForm.ZIP_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have ZIP Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.ZIP_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('ZIP value is not inserted properly')

    def enter_captcha_answer(self, value):
        LOGGER.info("Enter CAPTCHA value: " + value)
        element = self.find_element(OptInOptOutForm.CAPTCHA_ANSWER_INPUT)
        element.send_keys(value)
        # Ignoring captcha assertion for now
        # LOGGER.info("Should have CAPTCHA Input Text Equal to: " + value)
        # input_text = self.find_element(OptInOptOutForm.CAPTCHA_ANSWER_INPUT).get_attribute('value')
        # assert input_text == value, LOGGER.error('CAPTCHA value is not inserted properly')

    def clear_captcha_answer(self):
        LOGGER.info("Clear CAPTCHA value")
        element = self.find_element(OptInOptOutForm.CAPTCHA_ANSWER_INPUT)
        element.clear()


    def enter_middle_name(self, value):
        LOGGER.info("Enter MIDDLE NAME value: " + value)
        element = self.find_element(OptInOptOutForm.MIDDLE_NAME_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have MIDDLE NAME Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.MIDDLE_NAME_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('MIDDLE NAME value is not inserted properly')

    def enter_date_of_birth(self, value):
        LOGGER.info("Enter DATE OF BIRTH value: " + value)
        element = self.find_element(OptInOptOutForm.DATE_OF_BIRTH_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have DATE OF BIRTH Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.DATE_OF_BIRTH_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('DATE OF BIRTH value is not inserted properly')

    def enter_apt_or_suite(self, value):
        LOGGER.info("Enter APT. or SUITE value: " + value)
        element = self.find_element(OptInOptOutForm.APT_SUITE_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have APT. or SUITE Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.APT_SUITE_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('APT. or SUITE value is not inserted properly')

    def enter_telephone(self, value):
        LOGGER.info("Enter TELEPHONE value: " + value)
        element = self.find_element(OptInOptOutForm.TELEPHONE_INPUT)
        element.send_keys(value)
        LOGGER.info("Should have TELEPHONE Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.TELEPHONE_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('TELEPHONE value is not inserted properly')

    def is_displayed_captcha_error(self):
        LOGGER.info("Check if CAPTCHA ERROR is displayed....")
        try:
            self.find_element(OptInOptOutForm.CAPTCHA_ERROR_TXT, time=2)
            return bool(True)
        except:
            return bool(False)

    def is_displayed_dropdown_state_options(self):
        LOGGER.info("Check if STATE Dropdown OPTIONS are displayed....")
        try:
            self.find_element(OptInOptOutForm.STATE_DROPDOWN_OPTIONS, time=2)
            return bool(True)
        except:
            return bool(False)

    def is_displayed_dropdown_sufix_options(self):
        LOGGER.info("Check if SUFIX Dropdown OPTIONS are displayed....")
        try:
            self.find_element(OptInOptOutForm.SUFFIX_DROPDOWN_OPTIONS, time=2)
            return bool(True)
        except:
            return bool(False)

    def open_state_dropdown_and_select(self, value):
        LOGGER.info("Open STATE DROPDOWN and SELECT value: " + value)
        self.open_state_dropdown()
        self.select_state_option(value)
        # TODO add dropdown validation
        # print("Should have STATE DROPDOWN Value Selected: " + value)
        # input_text = self.find_element(BasicInfoPage.STATE_SELECTED_VALUE).text
        # assert input_text == value, 'STATE DROPDOWN Value is not selected properly'

    def open_state_dropdown(self):
        LOGGER.info("Open STATE DROPDOWN")
        if self.is_displayed_dropdown_state_options() == bool(False):
            element = self.find_element(OptInOptOutForm.STATE_DROPDOWN_VALUE)
            element.click()

    def select_state_option(self, value):
        LOGGER.info("Select option from STATE DROPDOWN " + value)
        dropdown_elements = self.find_elements(OptInOptOutForm.STATE_DROPDOWN_OPTIONS)
        for option in dropdown_elements:
            if option.text == value:
                option.click()

    def open_suffix_dropdown_and_select(self, value):
        LOGGER.info("Open SUFFIX DROPDOWN and SELECT value: " + value)
        self.open_suffix_dropdown()
        self.select_suffix_option(value)
        # TODO add dropdown validation

    def open_suffix_dropdown(self):
        LOGGER.info("Open SUFFIX DROPDOWN")
        if self.is_displayed_dropdown_sufix_options() == bool(False):
            element = self.find_element(OptInOptOutForm.SUFFIX_DROPDOWN_VALUE)
            element.click()

    def select_suffix_option(self, value):
        LOGGER.info("Select option from SUFFIX DROPDOWN " + value)
        dropdown_elements = self.find_elements(OptInOptOutForm.SUFFIX_DROPDOWN_OPTIONS)
        for option in dropdown_elements:
            if option.text == value:
                option.click()

    def get_captcha_img_web_element(self):
        LOGGER.info("Return CAPTCHA Image WebElement")
        element = self.find_element(OptInOptOutForm.CAPTCHA_IMG)
        return element

    def click_confirm_button(self):
        LOGGER.info("Click on Button: CONFIRM")
        element = self.find_element(OptInOptOutForm.CONFIRM_BTN)
        element.click()

    def should_see_basic_info_page(self):
        LOGGER.info("Should see Basic Info Page")
        try:
            self.find_element(OptInOptOutForm.FIRST_NAME_INPUT, time=2)
            self.find_element(OptInOptOutForm.LAST_NAME_INPUT, time=2)
            self.find_element(OptInOptOutForm.SSN1_INPUT, time=2)
            self.find_element(OptInOptOutForm.SSN2_INPUT, time=2)
            self.find_element(OptInOptOutForm.SSN3_INPUT, time=2)
            self.find_element(OptInOptOutForm.STREET_ADDRESS_INPUT, time=2)
            self.find_element(OptInOptOutForm.CITY_INPUT, time=2)
            self.find_element(OptInOptOutForm.ZIP_INPUT, time=2)
            self.find_element(OptInOptOutForm.CAPTCHA_IMG, time=2)
            self.find_element(OptInOptOutForm.CAPTCHA_ANSWER_INPUT, time=2)
        except:
            return bool(False)

    def captcha_input_should_have_value(self, value):
        LOGGER.info("Should have CAPTCHA Input Text Equal to: " + value)
        input_text = self.find_element(OptInOptOutForm.CAPTCHA_ANSWER_INPUT).get_attribute('value')
        assert input_text == value, LOGGER.error('CAPTCHA value is not inserted properly')
        return bool(True)

    def get_current_captcha_base64_string(self):
        LOGGER.info("Get Current captcha base64 value")
        captcha_base64_attribute_value: str = self.find_element(OptInOptOutForm.CAPTCHA_IMG).get_attribute('src')
        captcha_base64_value = captcha_base64_attribute_value.replace("data:image/png;base64,", "")
        return captcha_base64_value
