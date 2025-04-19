import base64
import os
import imghdr
import time
import random
import requests
import pathlib
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,\
    TablePageLocators, ButtonsPageLocators, LinksPageLocators, DownloadPageLocators, DynamicElementsPageLocators
from generator.generator import generated_person, generated_file


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step("Fill in All Fields")
    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        with allure.step("Fill all fields"):
            self.element_is_visible(locator=self.locators.FULL_NAME).send_keys(full_name)
            self.element_is_visible(locator=self.locators.EMAIL).send_keys(email)
            self.element_is_visible(locator=self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.element_is_visible(locator=self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            element = self.element_is_clickable(locator=self.locators.SUBMIT)
        with allure.step("Click Submit From"):
            self.go_to_element(element=element).click()
        return full_name, email, current_address, permanent_address

    @allure.step("Check Filled Form")
    def check_filled_form(self):
        full_name = self.element_is_present(locator=self.locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(locator=self.locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(locator=self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(locator=self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address


class CheckboxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step("Open Full List")
    def open_full_list(self):
        element = self.element_is_visible(locator=self.locators.EXPAND_ALL_BUTTON)
        self.go_to_element(element=element).click()

    @allure.step("Click random checkbox")
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(locator=self.locators.ITEM_LIST)
        for i in range(3):
            with allure.step(f"Select random checkbox {i}"):
                item = item_list[random.randint(1, 15)]
                print(f"item {item.text}")
                item.click()

    @allure.step("Get Checked items")
    def get_checked_items(self):
        item_list = self.elements_are_present(locator=self.locators.CHECKED_ITEMS)
        data = []
        for item in item_list:
            title_item = item.find_element(By.XPATH, self.locators.TITLE_ITEM).text
            data.append(title_item.lower().replace(" ", "").replace(".doc", ""))
            print(title_item)
        return data

    @allure.step("Get Output Results")
    def get_output_result(self):
        item_list = self.elements_are_present(locator=self.locators.OUTPUT_RESULT)
        text = [item.text.lower() for item in item_list]
        return text


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step("Click Radio Button")
    def click_radio_button(self, choice):
        choices = {"yes": self.locators.YES_RADIOBUTTON, "no": self.locators.NO_RADIOBUTTON,
                  "impressive": self.locators.IMPRESSIVE_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step("Get output result")
    def get_output_result(self):
        return self.element_is_visible(self.locators.RESULT).text

class TablePage(BasePage):
    locators = TablePageLocators()

    @allure.step("Add new person")
    def add_new_person(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        with allure.step("Generate test data"):
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

    @allure.step("Check new person")
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step("Search in Table")
    def search(self, keyword):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        self.element_is_visible(self.locators.SEARCH).send_keys(keyword)
        for i in range(3):
            new_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
            if new_list != people_list:
                break
            else:
                time.sleep(1)

    @allure.step("Check Search Result")
    def check_search(self):
        delete_button = self.element_is_present(locator=self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.TABLE_ITEM).text.splitlines()
        print(row)
        return row

    @allure.step("Update Person")
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE).clear()
        self.element_is_visible(self.locators.AGE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    @allure.step("Delete person")
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    @allure.step("Check Deleted")
    def check_deleted(self):
        return self.element_is_present(self.locators.RESULT).text

    @allure.step("Change Row count")
    def select_rows_count(self):
        element = self.element_is_present(locator=self.locators.PAGE_COUNT_SELECT)
        self.go_to_element(element=element)
        select = Select(element)
        select.select_by_value('25')

    @allure.step("Get rows count")
    def get_rows_count(self):
        list_rows = self.elements_are_present(self.locators.TABLE_ROW)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    @allure.step("Click Buttons")
    def click_buttons(self):
        self.element_is_visible(self.locators.CLICK_BUTTON).click()
        text = self.element_is_visible(self.locators.CLICK_TEXT).text

        element = self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON)
        self.action_double_click(element)
        text2 = self.element_is_visible(self.locators.DOUBLE_CLICK_TEXT).text

        element = self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON)
        self.action_right_click(element)
        text3 = self.element_is_visible(self.locators.RIGHT_CLICK_TEXT).text
        return [text, text2, text3]


class LinksPage(BasePage):
    locators = LinksPageLocators()

    @allure.step("Click New Tab")
    def click_new_tab_simlpe_link(self):
        element = self.element_is_visible(self.locators.SIMPLE_LINK)
        link = element.get_attribute('href')
        response = requests.get(link)
        if response.status_code == 200:
            element.click()
            self.switch_to_new_tab(1)
            url = self.driver.current_url
            return link, url
        else:
            print(f"STATUS CODE {response.status_code}")

    @allure.step("Click Broken Link")
    def check_broken_link(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            self.element_is_visible(self.locators.BAD_REQUEST_LINK).click()
        else:
            return response.status_code


class DownloadPage(BasePage):
    locators = DownloadPageLocators()

    @allure.step("Download File")
    def download_file(self):
        element = self.element_is_present(self.locators.DOWNLOAD_URL)
        link = element.get_attribute('href')
        link_base64 = base64.b64decode(link)
        current_dir = pathlib.Path(__file__).parent
        path = os.path.join(current_dir, "tmp.jpg")
        with open(path, 'wb+') as f:
            offset = link_base64.find(b'\xff\xd8')
            f.write(link_base64[offset:])
            os.path.exists(path)
            f.close()
        image_type = imghdr.what(path)
        with allure.step("Remove File"):
            os.remove(path)
        return image_type

    @allure.step("Upload File")
    def upload_file(self):
        file_path = generated_file()
        self.element_is_present(self.locators.UPLOAD_INPUT).send_keys(file_path)
        os.remove(file_path)
        return self.element_is_visible(self.locators.FILE_TEXT).text


class DynamicElementsPage(BasePage):
    locators = DynamicElementsPageLocators()

    @allure.step("Change color")
    def check_changed_color(self):
        button = self.element_is_present(locator=self.locators.BUTTON_COLOR_CHANGE)
        css_before = button.value_of_css_property('color')
        count = 0
        for i in range(10):
            with allure.step(f"Change color iter {i}"):
                button = self.element_is_present(locator=self.locators.BUTTON_COLOR_CHANGE)
                css_after = button.value_of_css_property('color')
                if css_after != css_before:
                    break
                else:
                    time.sleep(1)
                    count += 1
        return css_before, css_after, count

