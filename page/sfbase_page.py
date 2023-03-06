from selenium.webdriver.support.wait import WebDriverWait


class SFbase_page:

    def __int__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def _visit(self, url):
        self.driver.get(url)
