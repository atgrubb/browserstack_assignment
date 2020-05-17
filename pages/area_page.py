from enum import Enum
from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.web_driver import WebDriver


class AreaPage(WebDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    class Locators(Enum):
            AREA_HEADER = ("//div[@class='regular-area']/h2[@class='area']", By.XPATH)
            SEARCH_CRAIGSLIST = ("query", By.ID)

    class HousingLocators(Enum):
        HOUSING_HEADER = ("//a[@class='hhh']", By.XPATH)
        APTS_HOUSING = ("//a[@class='apa']", By.XPATH)
        HOUSING_SWAP = ("//a[@class='swp']", By.XPATH)
        HOUSING_WANTED = ("//a[@class='hsw']", By.XPATH)
        OFFICE_COMMERCIAL = ("//a[@class='off']", By.XPATH)
        PARKING_STORAGE = ("//a[@class='prk']", By.XPATH)
        REAL_ESTATE_FOR_SALE = ("//a[@class='rea']", By.XPATH)
        ROOMS_SHARED = ("//a[@class='roo']", By.XPATH)
        ROOMS_WANTED = ("//a[@class='sha']", By.XPATH)
        SUBLETS_TEMPORARY = ("//a[@class='sub']", By.XPATH)
        VACATION_RENTALS = ("//a[@class='vac']", By.XPATH)

    class JobsLocators(Enum):
        JOBS_HEADER = ("//a[@class='jjj']", By.XPATH)
        ACCOUNTING_FINANCE = ("//a[@class='acc']", By.XPATH)
        ADMIN_OFFICE = ("//a[@class='ofc']", By.XPATH)
        ARCH_ENGINEERING = ("//a[@class='egr']", By.XPATH)
        ART_MEDIA_DESIGN = ("//a[@class='med']", By.XPATH)
        BIOTECH_SCIENCE = ("//a[@class='sci']", By.XPATH)
        BUSINESS_MGMT = ("//a[@class='bus']", By.XPATH)
        CUSTOMER_SERVICE = ("//a[@class='csr']", By.XPATH)
        EDUCATION = ("//a[@class='edu']", By.XPATH)
        ETC_MISC = ("//a[@class='etc']", By.XPATH)
        FOOD_BEV_HOSP = ("//a[@class='fbh']", By.XPATH)
        GENERAL_LABOR = ("//a[@class='lab']", By.XPATH)
        GOVERNMENT = ("//a[@class='gov']", By.XPATH)
        HUMAN_RESOURCES = ("//a[@class='hum']", By.XPATH)
        LEGAL_PARALEGAL = ("//a[@class='lgl']", By.XPATH)
        MANUFACTURING = ("//a[@class='mnu']", By.XPATH)
        MARKETING_PR_AD = ("//a[@class='mar']", By.XPATH)
        MEDICAL_HEALTH = ("//a[@class='hea']", By.XPATH)
        NONPROFIT_SECTOR = ("//a[@class='npo']", By.XPATH)
        REAL_ESTATE = ("//a[@class='rej']", By.XPATH)
        RETAIL_WHOLESALE = ("//a[@class='ret']", By.XPATH)
        SALES_BIZ_DEV = ("//a[@class='sls']", By.XPATH)
        SALON_SPA_FITNESS = ("//a[@class='spa']", By.XPATH)
        SECURITY = ("//a[@class='sec']", By.XPATH)
        SKILLED_TRADE_CRAFT = ("//a[@class='trd']", By.XPATH)
        SOFTWARE_QA_DBA = ("//a[@class='sof']", By.XPATH)
        SYSTEMS_NETWORK = ("//a[@class='sad']", By.XPATH)
        TECHNICAL_SUPPORT = ("//a[@class='tch']", By.XPATH)
        TRANSPORT = ("//a[@class='trp']", By.XPATH)
        TV_FILM_VIDEO = ("//a[@class='tfr']", By.XPATH)
        WEB_INFO_DESIGN = ("//a[@class='web']", By.XPATH)
        WRITING_EDITING = ("//a[@class='wri']", By.XPATH)

    # ACTIONS
    def click(self, locator=Locators):
        self.click_element(locator.value, locator.value[1])

    def click_housing_locator(self, locator=HousingLocators):
        self.click_element(locator.value, locator.value[1])

    def click_jobs_locator(self, locator=JobsLocators):
        self.click_element(locator.value, locator.value[1])

    def send_keys_search_craigslist(self):
        self.send_keys_element(self.Locators.SEARCH_CRAIGSLIST.value, self.Locators.SEARCH_CRAIGSLIST.value[1])

