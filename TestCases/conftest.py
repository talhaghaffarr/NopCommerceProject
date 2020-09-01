from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
        driver.implicitly_wait(5)
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        # driver = webdriver.Firefox()
        print("Launching Opera Browser")
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        # driver = webdriver.Firefox()
        print("Launching Edge Browser")
    elif browser == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())
        # driver = webdriver.Firefox()
        print("Launching IE Browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
        driver.implicitly_wait(5)
        driver.maximize_window()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Pytest Html Report #
# Html Command: --html=Reports/report.html
# It is a Hook For Adding Environment info to Html Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Talha'
# It is a Hook to delete/Modify Environment info Html Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

