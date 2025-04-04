import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,\
    TablePageLocators, ButtonsPageLocators
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

    def add_new_person(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL_NAME).send_keys(email)
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SALARY).send_keys(salary)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search(self, keyword):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        self.element_is_visible(self.locators.SEARCH).send_keys(keyword)
        for i in range(3):
            new_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
            if new_list != people_list:
                break
            else:
                time.sleep(1)

    def check_search(self):
        delete_button = self.element_is_present(locator=self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.TABLE_ITEM).text.splitlines()
        print(row)
        return row

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.RESULT).text

    def select_rows_count(self):
        element = self.element_is_present(locator=self.locators.PAGE_COUNT_SELECT)
        self.go_to_element(element=element)
        select = Select(element)
        select.select_by_value('25')

    def get_rows_count(self):
        list_rows = self.elements_are_present(self.locators.TABLE_ROW)
        print(f"DEBUG {list_rows}")
        return len(list_rows)

class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_buttons(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()
        time.sleep(30)
        text = self.element_is_visible(self.locators.CLICK_TEXT).text

        element = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.action_double_click(element)
        text2 = self.element_is_visible(self.locators.DOUBLE_CLICK_TEXT).text

        element = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        self.action_right_click(element)
        text3 = self.element_is_visible(self.locators.RIGHT_CLICK_TEXT).text
        return [text, text2, text3]
