import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-ssl-errors')
    options.accept_insecure_certs = True
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.datetime.now()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
