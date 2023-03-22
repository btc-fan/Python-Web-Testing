import os
import datetime
import fnmatch
import jsonlines

from data_models.Base64ModelClass import Failed_Captcha
from utils.logger import LOGGER
from utils.paths import CAPTCHA_DOWNLOAD_FOLDER, JSON_DOWNLOAD_BASE64
from pages.OptInOptOutForm import BasicInfoHelper
from pages.DashboardPage import DashboardHelper
from pages.SelectionPage import SelectionHelper


def navigate_to_captcha_screen(browser):
    on_dashboard_main_page = DashboardHelper(browser)
    on_selection_page = SelectionHelper(browser)
    on_basic_info = BasicInfoHelper(browser)

    on_dashboard_main_page.go_to_website()
    on_dashboard_main_page.click_here_btn()
    on_selection_page.click_permanent_opt_out_radio_btn()
    on_selection_page.click_continue_btn()
    on_basic_info.should_see_basic_info_page()


def download_captchas(browser, captchas_amount, captcha_download_folder=CAPTCHA_DOWNLOAD_FOLDER.replace("/utils", "")):
    on_basic_info = BasicInfoHelper(browser)
    while len(fnmatch.filter(os.listdir(captcha_download_folder), '*.png')) <= captchas_amount:
        captcha_png = on_basic_info.get_captcha_img_web_element().screenshot_as_png
        LOGGER.info("Trying to save Captcha to path:\n" + captcha_download_folder)
        file_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
        with open(captcha_download_folder + file_name, 'wb') as f:
            f.write(captcha_png)
        LOGGER.info("Captcha Successfully Saved to path:\n" +
                    captcha_download_folder + file_name)
        on_basic_info.getDriver().refresh()


def save_current_captcha_png(browser, captcha_download_folder=CAPTCHA_DOWNLOAD_FOLDER):
    on_basic_info = BasicInfoHelper(browser)

    # In case empty, save to default download folder
    if not captcha_download_folder:
        captcha_download_folder = CAPTCHA_DOWNLOAD_FOLDER

    captcha_img = on_basic_info.get_captcha_img_web_element()
    captcha_png = captcha_img.screenshot_as_png
    LOGGER.info("Trying to save Captcha to path:\n" + captcha_download_folder)
    fileName = datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
    with open(captcha_download_folder + fileName, 'wb') as f:
        f.write(captcha_png)
    LOGGER.info("Captcha Successfully Saved to path:\n" +
                captcha_download_folder + fileName)
    return captcha_download_folder + fileName


def save_current_base64_captcha(browser, captcha_json_file=JSON_DOWNLOAD_BASE64):
    # base64_object = Captcha
    on_basic_info = BasicInfoHelper(browser)

    # In case empty, save to default download folder
    if not captcha_json_file:
        captcha_json_file = JSON_DOWNLOAD_BASE64
    LOGGER.info("Trying to save Captcha Base64 to Json path:\n" + captcha_json_file)

    captcha_base_64_value = on_basic_info.get_current_captcha_base64_string()
    base64_object = Failed_Captcha(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"), captcha_base_64_value)

    with open(captcha_json_file, 'wb') as f:
        writer = jsonlines.Writer(f)
        writer.write(base64_object.__dict__)
        writer.close()

    LOGGER.info("Captcha Successfully Saved to path:\n" + captcha_json_file)
