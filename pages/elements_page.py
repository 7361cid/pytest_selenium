import time
import random
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,\
    TablePageLocators
from generator.generator import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(locator=self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(locator=self.locators.EMAIL).send_keys(email)
        self.element_is_visible(locator=self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(locator=self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        element = self.element_is_clickable(locator=self.locators.SUBMIT)
        self.go_to_element(element=element).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(locator=self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(locator=self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(locator=self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(locator=self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckboxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        element = self.element_is_visible(locator=self.locators.EXPAND_ALL_BUTTON)
        self.go_to_element(element=element).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(locator=self.locators.ITEM_LIST)
        for i in range(3):
            item = item_list[random.randint(1, 15)]
            print(f"item {item.text}")
            item.click()

    def get_checked_items(self):
        item_list = self.elements_are_present(locator=self.locators.CHECKED_ITEMS)
        data = []
        for item in item_list:
            title_item = item.find_element(By.XPATH, self.locators.TITLE_ITEM).text
            data.append(title_item.lower().replace(" ", "").replace(".doc", ""))
            print(title_item)
        return data

    def get_output_result(self):
        item_list = self.elements_are_present(locator=self.locators.OUTPUT_RESULT)
        text = [item.text.lower() for item in item_list]
        return text


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {"yes": self.locators.YES_RADIOBUTTON, "no": self.locators.NO_RADIOBUTTON,
                  "impressive": self.locators.IMPRESSIVE_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_visible(self.locators.RESULT).text

class TablePage(BasePage):
    locators = TablePageLocators()