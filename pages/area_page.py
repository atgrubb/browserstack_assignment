from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

class AreaPage:
    def __init__(self, driver):
        self.driver = driver

    # LOCATORS
    # Each locator class contains tuples of the format (by=By.ID, value).
    # Example usage:
    # locator = self.HousingLocators.HOUSING_HEADER
    # element = self.driver.find_element(*locator)

    class GeneralLocators:
        AREA_HEADER = (By.XPATH, "//div[@class='regular-area']/h2[@class='area']")
        SEARCH_CRAIGSLIST = (By.ID, "query")

    class HousingLocators:
        HOUSING_HEADER = (By.XPATH, "//a[@class='hhh']")
        APTS_HOUSING = (By.XPATH, "//a[@class='apa']")
        HOUSING_SWAP = (By.XPATH, "//a[@class='swp']")
        HOUSING_WANTED = (By.XPATH, "//a[@class='hsw']")
        OFFICE_COMMERCIAL = (By.XPATH, "//a[@class='off']")
        PARKING_STORAGE = (By.XPATH, "//a[@class='prk']")
        REAL_ESTATE_FOR_SALE = (By.XPATH, "//a[@class='rea']")
        ROOMS_SHARED = (By.XPATH, "//a[@class='roo']")
        ROOMS_WANTED = (By.XPATH, "//a[@class='sha']")
        SUBLETS_TEMPORARY = (By.XPATH, "//a[@class='sub']")
        VACATION_RENTALS = (By.XPATH, "//a[@class='vac']")

    class JobsLocators:
        JOBS_HEADER = (By.XPATH, "//a[@class='jjj']")
        ACCOUNTING_FINANCE = (By.XPATH, "//a[@class='acc']")
        ADMIN_OFFICE = (By.XPATH, "//a[@class='ofc']")
        ARCH_ENGINEERING = (By.XPATH, "//a[@class='egr']")
        ART_MEDIA_DESIGN = (By.XPATH, "//a[@class='med']")
        BIOTECH_SCIENCE = (By.XPATH, "//a[@class='sci']")
        BUSINESS_MGMT = (By.XPATH, "//a[@class='bus']")
        CUSTOMER_SERVICE = (By.XPATH, "//a[@class='csr']")
        EDUCATION = (By.XPATH, "//a[@class='edu']")
        ETC_MISC = (By.XPATH, "//a[@class='etc']")
        FOOD_BEV_HOSP = (By.XPATH, "//a[@class='fbh']")
        GENERAL_LABOR = (By.XPATH, "//a[@class='lab']")
        GOVERNMENT = (By.XPATH, "//a[@class='gov']")
        HUMAN_RESOURCES = (By.XPATH, "//a[@class='hum']")
        LEGAL_PARALEGAL = (By.XPATH, "//a[@class='lgl']")
        MANUFACTURING = (By.XPATH, "//a[@class='mnu']")
        MARKETING_PR_AD = (By.XPATH, "//a[@class='mar']")
        MEDICAL_HEALTH = (By.XPATH, "//a[@class='hea']")
        NONPROFIT_SECTOR = (By.XPATH, "//a[@class='npo']")
        REAL_ESTATE = (By.XPATH, "//a[@class='rej']")
        RETAIL_WHOLESALE = (By.XPATH, "//a[@class='ret']")
        SALES_BIZ_DEV = (By.XPATH, "//a[@class='sls']")
        SALON_SPA_FITNESS = (By.XPATH, "//a[@class='spa']")
        SECURITY = (By.XPATH, "//a[@class='sec']")
        SKILLED_TRADE_CRAFT = (By.XPATH, "//a[@class='trd']")
        SOFTWARE_QA_DBA = (By.XPATH, "//a[@class='sof']")
        SYSTEMS_NETWORK = (By.XPATH, "//a[@class='sad']")
        TECHNICAL_SUPPORT = (By.XPATH, "//a[@class='tch']")
        TRANSPORT = (By.XPATH, "//a[@class='trp']")
        TV_FILM_VIDEO = (By.XPATH, "//a[@class='tfr']")
        WEB_INFO_DESIGN = (By.XPATH, "//a[@class='web']")
        WRITING_EDITING = (By.XPATH, "//a[@class='wri']")

    # ACTIONS

    def click(self, locator=GeneralLocators.AREA_HEADER):
        element = self.driver.find_element(*locator)
        element.click()

    def click_housing_locator(self, locator=HousingLocators.HOUSING_HEADER):
        element = self.driver.find_element(*locator)
        element.click()
        return SearchPage(self.driver)

    def click_jobs_locator(self, locator=JobsLocators.JOBS_HEADER):
        element = self.driver.find_element(*locator)
        element.click()
        return SearchPage(self.driver)

    def send_keys_search_craigslist(self, data):
        locator = self.GeneralLocators.SEARCH_CRAIGSLIST
        element = self.driver.find_element(*locator)
        element.send_keys(data)
        element.submit()
        return SearchPage(self.driver)
