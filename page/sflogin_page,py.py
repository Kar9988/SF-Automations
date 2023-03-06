from sfbase_page import SFbase_page
from contants import sflogin_page_constant


class LoginPage(SFbase_page):

    def __init__(self, driver, url=sflogin_page_constant.LOGIN_URL):
        SFbase_page.__init__(self.driver)
        self.driver = driver
        self.load(url)

    def load(self, url):
        self._visit(url)
