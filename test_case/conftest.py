import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

@pytest.fixture()
def setup(browser):
    baseURL = "https://dev.catexpert.ab-inbev.com/home"
    
    display = Display(visible=0, size=(800, 800))  
    display.start()
    driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get(baseURL)

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

def pytest_html_report_title(report):
    report.title = "CatExpert.AI -- Automation Testing Report"

# It is hook for Adding Environment info to HTML Report
#@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._metadata.pop("Python_HOME", None)
    config._metadata.pop("Plugins", None)
    config._metadata.pop("Packages", None)
    config._metadata.pop("Python", None)
    config._metadata['Project Name'] = 'CatExpert.ai'
    #config._metadata['Module Name'] = 'Product Home Page'
    config._metadata['Tester Name'] = ''
    config.option.htmlpath = os.path.abspath(os.curdir) + "/reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
