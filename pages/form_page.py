import os
import random
import time

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators
from generator.generator import generated_person, generated_file, generated_date, format_date
from selenium.webdriver import Keys


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        file_path = generated_file()

        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        gender_dict = {"male": self.locators.GENDER_MALE, "female": self.locators.GENDER_FEMALE}
        genders = ["male", "female"]
        random_gender = random.choice(genders)
        phone = person_info.phone
        current_address = person_info.current_address
        bday = generated_date()
        hobbies_dict = {"music": self.locators.HOBBY_MUSIC, "sports": self.locators.HOBBY_SPORTS,
                        "reading": self.locators.HOBBY_READING}
        hobbies = ["music", "sports", "reading"]
        random_hobby = random.choice(hobbies)

        self.element_is_visible(locator=self.locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(locator=self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(locator=self.locators.EMAIL).send_keys(email)
        self.element_is_visible(locator=gender_dict[random_gender]).click()
        self.element_is_visible(locator=self.locators.PHONE_NUMBER).send_keys(phone)
        self.element_is_visible(locator=self.locators.BDAY).send_keys(bday)
        for i in range(10):
            time.sleep(0.1)
            self.element_is_visible(locator=self.locators.BDAY).send_keys(Keys.ARROW_LEFT)
        for i in range(15):
            time.sleep(0.1)
            self.element_is_visible(locator=self.locators.BDAY).send_keys(Keys.BACKSPACE)
        self.element_is_visible(locator=self.locators.BDAY).send_keys(Keys.RETURN)
        self.element_is_visible(locator=self.locators.SUBJECTS).send_keys("Maths")
        self.element_is_visible(locator=self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_present(locator=hobbies_dict[random_hobby]).click()
        self.element_is_present(locator=self.locators.PICTURE).send_keys(file_path)
        os.remove(file_path)
        self.element_is_visible(locator=self.locators.ADDRESS).send_keys(current_address)
        self.go_to_element(self.element_is_present(locator=self.locators.STATE_SELECT))
        self.element_is_visible(locator=self.locators.STATE_SELECT).click()
        self.element_is_visible(locator=self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(locator=self.locators.CITY_SELECT).click()
        self.element_is_visible(locator=self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        element = self.element_is_clickable(locator=self.locators.SUBMIT)
        self.go_to_element(element=element).click()
        return first_name, last_name, email, random_gender, phone, random_hobby, format_date(bday), current_address

    def get_data_from_table(self):
        name = self.element_is_visible(self.locators.TABLE_NAME).text
        email = self.element_is_visible(self.locators.TABLE_EMAIL).text
        gender = self.element_is_visible(self.locators.TABLE_GENDER).text.lower()
        phone = self.element_is_visible(self.locators.TABLE_PHONE).text
        bday = self.element_is_visible(self.locators.TABLE_BDAY).text
        subjects = self.element_is_visible(self.locators.TABLE_SUBJECTS).text
        hobbies = self.element_is_visible(self.locators.TABLE_HOBBIES).text.lower()
        picture = self.element_is_visible(self.locators.TABLE_PICTURE).text
        address = self.element_is_visible(self.locators.TABLE_ADDRESS).text
        state = self.element_is_visible(self.locators.TABLE_STATE).text
        return name, email, gender, phone, bday, subjects, hobbies, picture, address, state
