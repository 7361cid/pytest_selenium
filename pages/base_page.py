from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def element_are_visible(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        return element

    def element_is_present(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def elements_is_present(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return element

    def element_is_not_visible(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return element

    def element_is_clickable(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return element

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
