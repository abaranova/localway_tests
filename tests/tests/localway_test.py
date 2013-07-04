from wtframework.wtf.web.page import PageFactory
from tests.pages.home_page import HomePage
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER

__author__ = 'lxz'


class LocalwayTest(WTFBaseTest):

    webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
    webdriver.get("http://172.31.237.12/")
    google_page = PageFactory.create_page(HomePage, webdriver)
    google_page.search_for_what("1223456")
    google_page.search_for_where("1223456")
    google_page.search_button_click()
