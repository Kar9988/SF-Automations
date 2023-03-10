from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class SfBasePage:

    def __int__(self, driver):
        print(111)

        self.driver = driver
        self.driver.maximize_window()

    def _visit(self, url):
        print(222)
        self.driver.get(url)

    def _is_displayed(self, locator, timeout=0):
        print(333)

        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located(locator["by"], ["value"]))
            except TimeoutException:
                return False
            return True
        else:
            try:
                self.driver.find_element(locator["by"], locator["value"])
            except NoSuchElementException:
                return False
            return True
