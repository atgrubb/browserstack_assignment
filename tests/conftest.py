import pytest
from selenium import webdriver
from pages.area_page import AreaPage
import uuid


@pytest.yield_fixture(scope="class")
def setUpClass(request, browser_stack_enabled, browser, browser_version, os, os_version, name):
    # Set default for BrowserStack enabled
    if browser_stack_enabled is None:
        browser_stack_enabled = False

    if browser_stack_enabled:
        browser_stack_url = 'https://alangrubb1:mqyCphmri491xmxqBxq3@hub-cloud.browserstack.com/wd/hub'
        desired_capabilities = get_desired_capabilities(browser, browser_version, os, os_version, name)
        driver = webdriver.Remote(
            command_executor=browser_stack_url,
            desired_capabilities=desired_capabilities
        )
    else:
        if str(browser).lower() == "iexplorer":
            driver = webdriver.Ie()
        elif str(browser).lower() == "firefox":
            driver = webdriver.Firefox()
        elif str(browser).lower() == "chrome":
            driver = webdriver.Chrome()
        elif str(browser).lower() == "safari":
            driver = webdriver.Safari()
        else:
            driver = webdriver.Chrome()

        driver.maximize_window()

    area_page = AreaPage(driver)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()


def get_desired_capabilities(browser, browser_version, os, os_version, name):
    # Configure defaults for desired capabilities
    if os is None:
        os = "OS X"
    if os_version is None:
        os_version = "Catalina"
    if browser is None:
        browser = "Safari"
    if browser_version is None:
        browser_version = "13"
    if name is None:
        name = "Test run: " + str(uuid.uuid4())

    # Declare desired capabilities with command line argument values (or default that were set just prior)
    desired_capabilities = {
        'os': os,
        'os_version': os_version,
        'browser': browser,
        'browser_version': browser_version,
        'name': name,
    }

    return desired_capabilities


def pytest_addoption(parser):
    parser.addoption("--browser-stack-Enabled", help="Execute tests on BrowserStack. Default set to 'False'.")
    parser.addoption("--browser", help="Browser within which to execute tests e.g. 'Safari'.")
    parser.addoption("--browser-version", help="Browser version to execute on e.g. '13'.")
    parser.addoption("--os", help="Operating system to execute on e.g. 'OS X'.")
    parser.addoption("--os-version", help="Operating system version e.g. 'Catalina'.")
    parser.addoption("--name", help="Name for the test in the BrowserStack dashboard.")


@pytest.fixture(scope="session")
def browser_stack_enabled(request):
    return request.config.getoption("--browser-stack-Enabled")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def browser_version(request):
    return request.config.getoption("--browser-version")


@pytest.fixture(scope="session")
def os(request):
    return request.config.getoption("--os")


@pytest.fixture(scope="session")
def os_version(request):
    return request.config.getoption("--os-version")


@pytest.fixture(scope="session")
def name(request):
    return request.config.getoption("--name")
