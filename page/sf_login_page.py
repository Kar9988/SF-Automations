from page.sf_base_page import SfBasePage
from contants import assertion_messages_constants, sf_login_page_constant


class LoginPage(SfBasePage):

    def __init__(self, driver, url=sf_login_page_constant.LOGIN_URL):
        SfBasePage.__init__(self.driver)
        self.driver = driver

        self.load(url)

    def load(self, url):
        print(555)
        self._visit(url)

        assert self.is_loaded, assertion_messages_constants.PAGE_NOT_LOADED

    def is_loaded(self, locator=sf_login_page_constant.LOGIN_URL):
        print(666)
        self._is_displayed(locator, 2)
