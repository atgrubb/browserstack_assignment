from selenium.common.by import By
from utilities.web_driver import WebDriver


class AreaPage(WebDriver):
    def __init__(self):
        super().__init__(driver)
        self.driver = driver

    # locators
    _area_header = "//div[@class='regular-area']/h2[@class='area']"

    # housing locators
    _housing_header = "//div[@id='hhh']/h4/a/span"
    _apts_housing = ""
    _housing_swap = ""
    _housing_wanted = ""
    _office_commercial = ""
    _parking_storage = ""
    _real_estate_for_sale = ""
    _rooms_shared = " "
    _rooms_wanted = ""
    _sublets_temporary = ""
    _vacation_rentals = ""

    # jobs locators
    _jobs_header = "//div[@id='jjj']/h4/a/span"
    _accounting_finance = ""
    _admin_office = ""
    _arch_engineering = ""
    _art_media_design = ""
    _biotech_science = ""
    _business_mgmt = ""
    _customer_service = ""
    _education = ""
    _etc_misc = ""
    _food_bev_hosp = ""
    _general_labor = ""
    _government = ""
    _human_resources = ""
    _legal_paralegal = ""
    _manufacturing = ""
    _marketing_pr_ad = ""
    _medical_health = ""
    _nonprofit_sector = ""
    _real_estate = ""
    _retail_wholesale = ""
    _sales_biz_dev = ""
    _salon_spa_fitness = ""
    _security = ""
    _skilled_trade_craft = ""
    _software_qa_dba = ""
    _systems_network = ""
    _technical_support = ""
    _transport = ""
    _tv_film_video = ""
    _web_info_design = ""
    _writing_editing = ""
