from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from traceback import print_stack

class WebDriver():
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator, by=By.ID):
        element = self.driver.find_element(by, locator)
        element.click()

    def send_keys_element(self, data, locator, by=By.ID):
        element = self.driver.find_element(by, locator)
        element.send_keys(data)

    def wait_element(self, locator, by=By.ID, timeout=5, poll_frequency=0.2):
        element = None
        try:
            wait = WebDriverWait(self.driver,
                                 timeout,
                                 poll_frequency,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(expected_conditions.presence_of_element_located((by, locator)))
        except NoSuchElementException as exception:
            print("No such element after waiting " + timeout + " seconds.")
            print_stack()
        return element
