from asyncio import sleep

from selenium import webdriver
from pages.area_page import AreaPage
from pages.search_page import SearchPage
import unittest

class AreaTests(unittest.TestCase):
    BASE_URL = "https://richmond.craigslist.org/"
    area_page = None
    driver = None

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