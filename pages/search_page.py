from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    # LOCATORS
    # Each locator class contains tuples of the format (by=By.ID, value).
    # Example usage:
    # locator = self.HousingLocators.HOUSING_HEADER
    # element = self.driver.find_element(*locator)

    class OptionsLocators:
        AREA_OPTIONS = (By.ID, "areaAbb")
        CATEGORIES_OPTIONS = (By.ID, "catAbb")
        SUBCATEGORIES_OPTIONS = (By.ID, "subcatAbb")

    class CategoriesOptionsLocators:
        COMMUNITY = (By.XPATH, "//select[@id='catAbb']/option[@value='ccc']")
        EVENTS = (By.XPATH, "//select[@id='catAbb']/option[@value='eee']")
        FOR_SALE = (By.XPATH, "//select[@id='catAbb']/option[@value='sss']")
        GIGS = (By.XPATH, "//select[@id='catAbb']/option[@value='ggg']")
        HOUSING = (By.XPATH, "//select[@id='catAbb']/option[@value='hhh']")
        JOBS = (By.XPATH, "//select[@id='catAbb']/option[@value='jjj']")
        RESUMES = (By.XPATH, "//select[@id='catAbb']/option[@value='rrr']")
        SERVICES = (By.XPATH, "//select[@id='catAbb']/option[@value='bbb']")

    class HousingSubCategoriesLocators:
        ALL = (By.XPATH, "//select[@id='subcatAbb']/option[@value='hhh']")
        APTS_HOUSING = (By.XPATH, "//select[@id='subcatAbb']/option[@value='apa']")
        HOUSING_SWAP = (By.XPATH, "//select[@id='subcatAbb']/option[@value='swp']]")
        OFFICE_COMMERCIAL = (By.XPATH, "//select[@id='subcatAbb']/option[@value='off']")
        PARKING_STORAGE = (By.XPATH, "//select[@id='subcatAbb']/option[@value='prk']")
        REAL_ESTATE_BY_BROKER = (By.XPATH, "//select[@id='subcatAbb']/option[@value='reb']")
        REAL_ESTATE_BY_OWNER = (By.XPATH, "//select[@id='subcatAbb']/option[@value='reo']")
        ROOMS_SHARED = (By.XPATH, "//select[@id='subcatAbb']/option[@value='roo']")
        SUBLETS_TEMPORARY = (By.XPATH, "//select[@id='subcatAbb']/option[@value='sub']")
        VACATION_RENTALS = (By.XPATH, "//select[@id='subcatAbb']/option[@value='vac']")
        WANTED_APTS = (By.XPATH, "//select[@id='subcatAbb']/option[@value='hou']")
        WANTED_REAL_ESTATE = (By.XPATH, "//select[@id='subcatAbb']/option[@value='rew']")
        WANTED_ROOM_SHARE = (By.XPATH, "//select[@id='subcatAbb']/option[@value='sha']")
        WANTED_SUBLET_TEMP = (By.XPATH, "//select[@id='subcatAbb']/option[@value='sbw']")

    # ACTIONS

    def verify_category_option_selected(self, option_locator=CategoriesOptionsLocators.COMMUNITY):
        # Get the categories drop down element
        category_locator = self.OptionsLocators.CATEGORIES_OPTIONS
        category_element = self.driver.find_element(*category_locator)

        # Get the currently selected option for the categories drop down
        selected_option_element = Select(category_element).first_selected_option

        # Get the element for the option with which this method was called i.e. the option we expect to be selected
        expected_option_element = self.driver.find_element(*option_locator)

        print(selected_option_element.text + " should be equal to " + expected_option_element.text)
        return selected_option_element.text == expected_option_element.text
