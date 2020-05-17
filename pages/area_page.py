from selenium.common.by import By
from utilities.web_driver import WebDriver


class AreaPage(WebDriver):
    def __init__(self):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    _area_header = "//div[@class='regular-area']/h2[@class='area']"

    # housing locators
    _housing_header = "//a[@class='hhh']"
    _apts_housing = "//a[@class='apa']"
    _housing_swap = "//a[@class='swp']"
    _housing_wanted = "//a[@class='hsw']"
    _office_commercial = "//a[@class='off']"
    _parking_storage = "//a[@class='prk']"
    _real_estate_for_sale = "//a[@class='rea']"
    _rooms_shared = "//a[@class='roo']"
    _rooms_wanted = "//a[@class='sha']"
    _sublets_temporary = "//a[@class='sub']"
    _vacation_rentals = "//a[@class='vac']"

    # jobs locators
    _jobs_header = "//a[@class='jjj']"
    _accounting_finance = "//a[@class='acc']"
    _admin_office = "//a[@class='ofc']"
    _arch_engineering = "//a[@class='egr']"
    _art_media_design = "//a[@class='med']"
    _biotech_science = "//a[@class='sci']"
    _business_mgmt = "//a[@class='bus']"
    _customer_service = "//a[@class='csr']"
    _education = "//a[@class='edu']"
    _etc_misc = "//a[@class='etc']"
    _food_bev_hosp = "//a[@class='fbh']"
    _general_labor = "//a[@class='lab']"
    _government = "//a[@class='gov']"
    _human_resources = "//a[@class='hum']"
    _legal_paralegal = "//a[@class='lgl']"
    _manufacturing = "//a[@class='mnu']"
    _marketing_pr_ad = "//a[@class='mar']"
    _medical_health = "//a[@class='hea']"
    _nonprofit_sector = "//a[@class='npo']"
    _real_estate = "//a[@class='rej']"
    _retail_wholesale = "//a[@class='ret']"
    _sales_biz_dev = "//a[@class='sls']"
    _salon_spa_fitness = "//a[@class='spa']"
    _security = "//a[@class='sec']"
    _skilled_trade_craft = "//a[@class='trd']"
    _software_qa_dba = "//a[@class='sof']"
    _systems_network = "//a[@class='sad']"
    _technical_support = "//a[@class='tch']"
    _transport = "//a[@class='trp']"
    _tv_film_video = "//a[@class='tfr']"
    _web_info_design = "//a[@class='web']"
    _writing_editing = "//a[@class='wri']"

    # GETTERS
    # housing getters
    def get_housing_anchor(self):
        return self.driver.find_element(By.XPATH, self._housing_header)

    def get_apts_housing_anchor(self):
        return self.driver.find_element(By.XPATH, self._apts_housing)

    def get_housing_swap_anchor(self):
        return self.driver.find_element(By.XPATH, self._housing_swap)

    def get_housing_wanted_anchor(self):
        return self.driver.find_element(By.XPATH, self._housing_wanted)

    def get_office_commercial_anchor(self):
        return self.driver.find_element(By.XPATH, self._office_commercial)

    def get_parking_storage_anchor(self):
        return self.driver.find_element(By.XPATH, self._parking_storage)

    def get_real_estate_for_sale_anchor(self):
        return self.driver.find_element(By.XPATH, self._real_estate_for_sale)

    def get_rooms_shared_anchor(self):
        return self.driver.find_element(By.XPATH, self._rooms_shared)

    def get_rooms_wanted_anchor(self):
        return self.driver.find_element(By.XPATH, self._rooms_wanted)

    def get_sublets_temporary_anchor(self):
        return self.driver.find_element(By.XPATH, self._sublets_temporary)

    def get_vacation_rentals_anchor(self):
        return self.driver.find_element(By.XPATH, self._vacation_rentals)

    # ACTIONS
