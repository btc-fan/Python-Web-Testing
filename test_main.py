import copy

from pages.SessionEndedPage import SessionEndedHelper
from pages.SuccessfulSubmissionPage import SuccessfulSubmissionHelper
from data_models.PersonModelClass import *
from utils.download_new_captchas_for_training import *
from utils.utils import inject_data
from pages.OptInOptOutForm import BasicInfoHelper
from conftest import *
import sys
import docker

test_data = inject_data()


@pytest.mark.parametrize("person_data", test_data)
def test_main(browser, person_data):

    CAPTCHA_RETRIES: int = 1
    SUCCESS : bool = False
    CAPTCHA_BASE64_STRING: str
    person_model = PersonModel.Schema().loads(json.dumps(person_data))
    on_basic_info = BasicInfoHelper(browser)
    on_successful_submission = SuccessfulSubmissionHelper(browser)
    on_session_ended = SessionEndedHelper(browser)

    # Docker Img for captcha bypass
    DOCKER_IMG_NAME = "captcha_bypass"
    docker_client = docker.from_env()


    # index = get_current_object_index_by_uuid(test_data, person_model.UUID)

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

    CAPTCHA_BASE64_STRING = on_basic_info.get_current_captcha_base64_string()

    captcha_bypass_docker_img_result = docker_client.containers.run(DOCKER_IMG_NAME, "--captcha_base64 " + CAPTCHA_BASE64_STRING, True)
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

        if ((on_basic_info.is_displayed_captcha_error() or len(captcha_answer) < 8)):
            # if on_session_ended.should_see_session_ended_page():
            #     LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            #     raise ValueError("USER IS ON SESSION ENDED PAGE")

            LOGGER.error("Wrong Captcha!!!, Going to make another retry.\nRETRY ATTEMPT: %d", CAPTCHA_RETRIES)

            pytest.captcha_response_object["img"] = CAPTCHA_BASE64_STRING
            pytest.captcha_response_object["success"] = SUCCESS
            pytest.captcha_response_array.append(copy.deepcopy(pytest.captcha_response_object))
            # response_data_object['attempts'] = CAPTCHA_RETRIES

            save_current_base64_captcha(browser, JSON_DOWNLOAD_BASE64)
            if CAPTCHA_RETRIES < 1:
                on_basic_info.clear_captcha_answer()
                on_basic_info.enter_captcha_answer(RANDOM_CAPTCHA)
                on_basic_info.click_confirm_button()
                CAPTCHA_RETRIES += 1

            # if on_successful_submission.should_see_successful_submission_page():
            #     LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            #     raise ValueError("!!!!! USER WAS REDIRECTED TO SUCCESSFULLY SUBMISSION FORM WITH RANDOM CAPTCHA VALUE " + RANDOM_CAPTCHA)

            CAPTCHA_BASE64_STRING = on_basic_info.get_current_captcha_base64_string()
            captcha_bypass_docker_img_result = docker_client.containers.run(DOCKER_IMG_NAME, "--captcha_base64 " + CAPTCHA_BASE64_STRING, True)
            captcha_answer = str(captcha_bypass_docker_img_result).replace("b", "").replace("'", "").replace("\\n", "")
            # captcha_answer = "kimpomrt"
            on_basic_info.enter_captcha_answer(captcha_answer)
            on_basic_info.click_confirm_button()
            CAPTCHA_RETRIES += 1
        else:
            LOGGER.info("Captcha Submission From is successfully\nRETRY ATTEMPTIONS: %d", CAPTCHA_RETRIES)
            SUCCESS = True
            pytest.captcha_response_object["img"] = CAPTCHA_BASE64_STRING
            pytest.captcha_response_object["success"] = SUCCESS
            pytest.captcha_response_array.append(copy.deepcopy(pytest.captcha_response_object))
            pytest.response_data_object['attempts'] = CAPTCHA_RETRIES
            break

    else:
        LOGGER.error("!!!!!! SUBMISSION FAILED !!!!!!!!!!!!!!!")
        pytest.response_data_object['UUID'] = person_model.UUID
        pytest.response_data_object['submitSuccess'] = SUCCESS
        pytest.response_data_object['attempts'] = CAPTCHA_RETRIES
        pytest.response_data_object['captcha'] = pytest.captcha_response_array
        pytest.response_data_object['responseMessage'] = "SUBMISSION_FAILED"
        raise ValueError("SUBMISSION FAILED RETRY ATTEMPTED: ",  CAPTCHA_RETRIES)

    on_successful_submission.should_see_successful_submission_page()
    LOGGER.info("!!!! USER SUCCESSFULLY SUBMITTED OPT OUT REQUEST !!!!")
    SUCCESS = True
    pytest.response_data_object['UUID'] = person_model.UUID
    pytest.response_data_object['submitSuccess'] = SUCCESS
    pytest.response_data_object['captcha'] = pytest.captcha_response_array
    pytest.response_data_object['responseMessage'] = "USER_SUCCESSFULLY_SUBMITTED"