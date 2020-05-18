from selenium import webdriver
from pages.area_page import AreaPage
from pages.search_page import SearchPage
import pytest


class TestAreaPage:
    BASE_URL = "https://richmond.craigslist.org/"
    area_page = None
    '''
    BROWSERSTACK_URL = 'https://alangrubb1:mqyCphmri491xmxqBxq3@hub-cloud.browserstack.com/wd/hub'
    desired_capabilities = {
        'os': 'OS X',
        'os_version': 'Catalina',
        'browser': 'Safari',
        'browser_version': '13',
        'name': "test ssl certs true",
    }
    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        desired_capabilities=desired_capabilities
    )
    '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get(self.BASE_URL)
        self.area_page = AreaPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_click_housing_header(self):
        search_page = self.area_page.click_housing_locator(AreaPage.HousingLocators.HOUSING_HEADER)
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.HOUSING)
        assert result is True

    def test_click_jobs_header(self):
        search_page = self.area_page.click_jobs_locator(AreaPage.JobsLocators.JOBS_HEADER)
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.JOBS)
        assert result is True

    def test_search_area_bicycle_for_sale(self):
        search_page = self.area_page.send_keys_search_craigslist("cannondale bicycle")
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.FOR_SALE)
        assert result is True
