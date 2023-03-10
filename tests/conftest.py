import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from page.sf_login_page import LoginPage
from contants.main_constant import BASE_URL


@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture
def launch_browser(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(BASE_URL)

    def quit():
        print(888)
        driver.quit()

    request.addfinalizer(quit())
    return driver


# @allure.severity(allure.severity_level.CRITICAL)
# @pytest.fixture(scope="module")
# def search_load(launch_browser):
#     search_load = SearchPage(launch_browser)
#     return search_load

@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture(scope="module")
def login_loaded(launch_browser):
    print(444)
    login_loaded = LoginPage(launch_browser)
    return login_loaded
