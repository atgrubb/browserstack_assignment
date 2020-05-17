from enum import Enum
from selenium.webdriver.common.by import By
from utilities.web_driver import WebDriver

class SearchPage(WebDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    class OptionsLocators(Enum):
        AREA_OPTIONS = ("areaAbb", By.ID)
        CATEGORIES_OPTIONS = ("catAbb", By.ID)
        SUBCATEGORIES_OPTIONS = ("subcatAbb", By.ID)

    class CategoriesOptionsLocators(Enum):
        COMMUNITY = ("//select[@id='catAbb']/option[@value='ccc']", By.XPATH)
        EVENTS = ("//select[@id='catAbb']/option[@value='eee']", By.XPATH)
        FOR_SALE = ("//select[@id='catAbb']/option[@value='sss']", By.XPATH)
        GIGS = ("//select[@id='catAbb']/option[@value='ggg']", By.XPATH)
        HOUSING = ("//select[@id='catAbb']/option[@value='hhh']", By.XPATH)
        JOBS = ("//select[@id='catAbb']/option[@value='jjj']", By.XPATH)
        RESUMES = ("//select[@id='catAbb']/option[@value='rrr']", By.XPATH)
        SERVICES = ("//select[@id='catAbb']/option[@value='bbb']", By.XPATH)

    class HousingSubCategoriesLocators(Enum):
        ALL = ("//select[@id='subcatAbb']/option[@value='hhh']", By.XPATH)
        APTS_HOUSING = ("//select[@id='subcatAbb']/option[@value='apa']", By.XPATH)
        HOUSING_SWAP = ("//select[@id='subcatAbb']/option[@value='swp']]", By.XPATH)
        OFFICE_COMMERCIAL = ("//select[@id='subcatAbb']/option[@value='off']", By.XPATH)
        PARKING_STORAGE = ("//select[@id='subcatAbb']/option[@value='prk']", By.XPATH)
        REAL_ESTATE_BY_BROKER = ("//select[@id='subcatAbb']/option[@value='reb']", By.XPATH)
        REAL_ESTATE_BY_OWNER = ("//select[@id='subcatAbb']/option[@value='reo']", By.XPATH)
        ROOMS_SHARED = ("//select[@id='subcatAbb']/option[@value='roo']", By.XPATH)
        SUBLETS_TEMPORARY = ("//select[@id='subcatAbb']/option[@value='sub']", By.XPATH)
        VACATION_RENTALS = ("//select[@id='subcatAbb']/option[@value='vac']", By.XPATH)
        WANTED_APTS = ("//select[@id='subcatAbb']/option[@value='hou']", By.XPATH)
        WANTED_REAL_ESTATE = ("//select[@id='subcatAbb']/option[@value='rew']", By.XPATH)
        WANTED_ROOM_SHARE = ("//select[@id='subcatAbb']/option[@value='sha']", By.XPATH)
        WANTED_SUBLET_TEMP = ("//select[@id='subcatAbb']/option[@value='sbw']", By.XPATH)
