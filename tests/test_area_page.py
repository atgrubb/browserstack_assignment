import unittest
from time import sleep

from pages.area_page import AreaPage
from pages.search_page import SearchPage
import pytest


@pytest.mark.usefixtures("setUpClass")
class TestAreaPage(unittest.TestCase):

    def setUp(self):
        base_url = "https://richmond.craigslist.org/"
        self.driver.get(base_url)

    @pytest.fixture(autouse=True)
    def objectSetup(self, setUpClass):
        self.area_page = AreaPage(self.driver)

    def test_click_housing_header(self):
        search_page = self.area_page.click_housing_locator(AreaPage.HousingLocators.HOUSING_HEADER)
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.HOUSING)
        sleep(3)
        assert result is True

    def test_click_jobs_header(self):
        search_page = self.area_page.click_jobs_locator(AreaPage.JobsLocators.JOBS_HEADER)
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.JOBS)
        sleep(3)
        assert result is True

    def test_search_area_bicycle_for_sale(self):
        search_page = self.area_page.send_keys_search_craigslist("cannondale bicycle")
        result = search_page.verify_category_option_selected(SearchPage.CategoriesOptionsLocators.FOR_SALE)
        sleep(3)
        assert result is True
