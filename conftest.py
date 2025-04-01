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
   # capabilities = {"acceptInsecureCerts": True, }
    driver = webdriver.Chrome(options=options)
    #webdriver.Chrome(chrome_options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
