from pages.SuccessfulSubmissionPage import SuccessfulSubmissionHelper
from data_models.PersonModelClass import *
from utils.download_new_captchas_for_training import navigate_to_captcha_screen
from utils.utils import inject_data
from pages.OptInOptOutForm import BasicInfoHelper
from conftest import *

test_data = inject_data()

@pytest.mark.parametrize("person_data", test_data)
def test_main(browser, person_data):

    person_model = PersonModel.Schema().loads(json.dumps(person_data))
    on_basic_info = BasicInfoHelper(browser)
    on_successful_submission = SuccessfulSubmissionHelper(browser)
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

    captcha_answer = "A1B2C3B4"
    on_basic_info.enter_captcha_answer(captcha_answer)
    on_basic_info.click_confirm_button()
    on_successful_submission.should_see_successful_submission_page()
    LOGGER.info("!!!! USER SUCCESSFULLY SUBMITTED OPT OUT REQUEST !!!!")
    SUCCESS = True
    pytest.response_data_object['UUID'] = person_model.UUID
    pytest.response_data_object['submitSuccess'] = SUCCESS
    pytest.response_data_object['captcha'] = pytest.captcha_response_array
    pytest.response_data_object['responseMessage'] = "USER_SUCCESSFULLY_SUBMITTED"