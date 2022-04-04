import pytest
from utils.download_new_captchas_for_training import *
from utils.confest import browser


def test_get_captchas(browser):
    navigate_to_captcha_screen(browser)
    download_captchas(browser, 100)


if __name__ == '__main__':
    pytest.main(["test_get_captchas.py", "-s"])
