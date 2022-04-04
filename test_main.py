import json

import pytest
# from captcha_model_training.CAPTCHA_object_detection import captcha_detection
from pages.SessionEndedPage import SessionEndedHelper
from pages.SuccessfulSubmissionPage import SuccessfulSubmissionHelper
from utils.data_models.PersonModelClass import *

from utils.download_new_captchas_for_training import *
from utils.variables import FAILED_CAPTCHA_DOWNLOAD_FOLDER, UTILS_FOLDER, DATA_MODEL_FOLDER
from pages.OptInOptOutForm import BasicInfoHelper
from utils.confest import browser
import sys
import docker

def test_main(browser):

    # Docker Img for captcha bypass
    image = "captcha_bypass"
    client = docker.from_env()

    CAPTCHA_RETRIES: int = 0
    json_file = open(DATA_MODEL_FOLDER + "person_data_model.json")
    person_data = json.load(json_file)
    person_model = PersonModel.Schema().loads(json.dumps(person_data))
    on_basic_info = BasicInfoHelper(browser)
    on_successful_submission = SuccessfulSubmissionHelper(browser)
    on_session_ended = SessionEndedHelper(browser)

    # client.containers.run(image,  "", True)

    navigate_to_captcha_screen(browser)
    on_basic_info.enter_first_name(person_model.firstname)
    on_basic_info.enter_last_name(person_model.lastname)
    on_basic_info.enter_full_ssn(person_model.ssn)
    on_basic_info.enter_street_address(person_model.address)
    on_basic_info.enter_city(person_model.city)
    on_basic_info.enter_zip(person_model.zip)
    on_basic_info.open_state_dropdown_and_select(person_model.state)
    # Optional fields
    on_basic_info.enter_date_of_birth(person_model.dob)
    on_basic_info.enter_apt_or_suite(person_model.apt)
    on_basic_info.enter_telephone(person_model.telephone)

    # captcha_img_png = save_current_captcha(browser)
    # captcha_answer = captcha_detection(captcha_img_png)
    captcha_answer = 'kimpomrt'

    captcha_base_64_value = on_basic_info.get_current_captcha_base64_string()
    captcha_bypass_docker_img_result = client.containers.run(image, "--captcha_base64 " + captcha_base_64_value, True)
    captcha_answer = str(captcha_bypass_docker_img_result).replace("b", "").replace("'", "").replace("\\n", "")
    on_basic_info.enter_captcha_answer(captcha_answer)
    # on_basic_info.captcha_input_should_have_value(captcha_answer)
    on_basic_info.click_confirm_button()

    while CAPTCHA_RETRIES < 3:
        # Random Test to trigger captcha reload. Dont try only numbers. If there are 8 numbers as captcha answer,
        # user will be redirected to SUCCESSFULL submission page.
        RANDOM_CAPTCHA = "kimpomrt"
        # TODO Refactor and simplify the retry logics
        # Make it recursive through switch. This might be as a default option
        #

        if ((on_basic_info.is_displayed_captcha_error() or len(captcha_answer) < 8)):
            # if on_session_ended.should_see_session_ended_page():
            #     LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            #     raise ValueError("USER IS ON SESSION ENDED PAGE")

            LOGGER.error("Wrong Captcha!!!, Going to make another retry.\nRETRY ATTEMPT: %d", CAPTCHA_RETRIES)
            save_current_base64_captcha(browser, JSON_DOWNLOAD_BASE64)
            if CAPTCHA_RETRIES < 1:
                on_basic_info.clear_captcha_answer()
                on_basic_info.enter_captcha_answer(RANDOM_CAPTCHA)
                on_basic_info.click_confirm_button()

            # if on_successful_submission.should_see_successful_submission_page():
            #     LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            #     raise ValueError("!!!!! USER WAS REDIRECTED TO SUCCESSFULLY SUBMISSION FORM WITH RANDOM CAPTCHA VALUE " + RANDOM_CAPTCHA)

            # captcha_img_png = save_current_captcha_png(browser)
            # captcha_answer = captcha_detection(captcha_img_png)
            # captcha_answer = "ZXC"
            captcha_base_64_value = on_basic_info.get_current_captcha_base64_string()
            captcha_bypass_docker_img_result = client.containers.run(image, "--captcha_base64 " + captcha_base_64_value, True)
            captcha_answer = str(captcha_bypass_docker_img_result).replace("b", "").replace("'", "").replace("\\n", "")
            on_basic_info.enter_captcha_answer(captcha_answer)
            on_basic_info.click_confirm_button()
            # on_basic_info.reloadPage()
            CAPTCHA_RETRIES += 1
        else:
            LOGGER.info("Captcha Submission From is successfully\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            break

    else:
        LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!")
        raise ValueError("SUBMISSION FAILED RETRY ATTEMPTED: ",  CAPTCHA_RETRIES)

    on_successful_submission.should_see_successful_submission_page()
    LOGGER.info("!!!! USER SUCCESSFULLY SUBMITTED OPT OUT REQUEST !!!!")

    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.FIRST_NAME, person_model.firstName)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.LAST_NAME, person_model.lastName)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.STREET_ADDRESS, person_model.streetAddress)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.CITY, person_model.city)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.ZIP_CODE, person_model.zip)


    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.SSN, person_model.ssn)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.STATE, person_model.state)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.MIDDLE_NAME, person_model.middleName)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.SUFFIX, person_model.suffix)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.DATE_OF_BIRTH, person_model.dateOfBirth)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.APT_OR_SUITE, person_model.aptSuite)
    # on_successful_submission.should_have_field_name_equal_to_value(
    #     FieldName.TELEPHONE, person_model.telephone)

    # on_successful_submission.get_successful_submission_field_names()
    # on_successful_submission.get_successful_submission_field_values()


if __name__ == '__main__':
    # unittest.main()
    pytest.main(["test_main.py", "-s"])
