from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def elements_are_visible(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def element_is_present(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def elements_are_present(self, locator, timeout=10):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def element_is_not_visible(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return element

    def element_is_clickable(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return element

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def action_double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def action_right_click(self, element):
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def switch_to_new_tab(self, i):
        self.driver.switch_to.window(self.driver.window_handles[i])

    def action_drag_and_drop_by_offset(self, element, x=0, y=0, is_locator=False):
        actions = ActionChains(self.driver)
        if is_locator:
            element = self.element_is_present(element)
        actions.drag_and_drop_by_offset(element, x, y).perform()

    def action_drag_and_drop_to_element(self, element_from, element_to):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_from, element_to)
        actions.perform()

    def action_hover(self, hover_element, is_locator=True):
        actions = ActionChains(self.driver)
        if is_locator:
            hover_element = self.element_is_present(hover_element)
        actions.move_to_element(hover_element).perform()
