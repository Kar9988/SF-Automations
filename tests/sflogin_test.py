import pytest
import allure
import time
import click
from selenium.webdriver.common.keys import Keys
from contants.sflogin_page_constant import *

@allure.title("Sportyfriend login page is tested! ")
@pytest.mark.regression

def sf_login_test(login_porcess):
    login_button_click = login_porcess.driver.find_element(LOGIN_BUTTON["by"], LOGIN_BUTTON["value"])
    login_button_click.click()
    email_field = login_porcess.driver.find_element(EMAIL_FIELD["by"], EMAIL_FIELD["value"])
    email_field.send_keys(CORRECT_EMAIL + Keys.ENTER)
