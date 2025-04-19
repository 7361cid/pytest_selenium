import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators,\
    ProgressBarPageLocators, SliderBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from generator.generator import get_random_color, get_date


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self):
        texts = []
        locators_list = [(self.locators.HEADER_1, self.locators.TEXT_1),
                         (self.locators.HEADER_2, self.locators.TEXT_2), (self.locators.HEADER_3, self.locators.TEXT_3)]
        for l in locators_list:
            element = self.element_is_visible(locator=l[0])
            self.go_to_element(element)
            element.click()
            time.sleep(1)
            try:
                text = self.element_is_visible(locator=l[1]).text
            except TimeoutException:
                element.click()
                time.sleep(1)
                text = self.element_is_visible(locator=l[1]).text
            texts.append(element.text)
            texts.append(text)
        return texts


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        colors = get_random_color()
        element = self.element_is_clickable(locator=self.locators.MULTI_INPUT)
        for c in colors:
            element.send_keys(c)
            element.send_keys(Keys.RETURN)
        return colors

    def delete_from_multi_input(self):
        count = len(self.elements_are_visible(locator=self.locators.MULTI_INPUT_VALUES))
        delete_buttons = self.elements_are_present(locator=self.locators.MULTI_VALUE_REMOVE)
        for b in delete_buttons:
            b.click()
            break
        count2 = len(self.elements_are_present(locator=self.locators.MULTI_INPUT_VALUES))
        return count, count2

    def get_multi_input_values(self):
        data = []
        elements = self.elements_are_visible(locator=self.locators.MULTI_INPUT_VALUES)
        for e in elements:
            data.append(e.text)
        return data

    def fill_input_single(self):
        color = get_random_color()[0]
        element = self.element_is_clickable(locator=self.locators.SINGLE_INPUT)
        element.send_keys(color)
        element.send_keys(Keys.RETURN)
        return color

    def check_single_color(self):
        element = self.element_is_visible(locator=self.locators.SINGLE_INPUT_VALUE)
        return element.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = get_date()
        input_date = self.element_is_visible(locator=self.locators.SELECT_DATE_INPUT)
        input_date_before = input_date.get_attribute('value')
        input_date.click()
        self.select_date_by_text(self.locators.SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.SELECT_YEAR, date.year)
        self.select_date_from_list(self.locators.SELECT_DAY_LIST, date.day)
        input_date_after = input_date.get_attribute('value')
        return input_date_before, input_date_after

    def select_date_and_time(self):
        date = get_date()
        input_date = self.element_is_visible(locator=self.locators.SELECT_DATE_AND_TIME_INPUT)
        input_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(locator=self.locators.DATE_AND_TIME_MONTH).click()
        self.select_date_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_visible(locator=self.locators.DATE_AND_TIME_YEAR).click()
        self.select_date_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)
        day = date.day
        if day[0] == "0":
            day = day[1:]
        self.select_date_from_list(self.locators.SELECT_DAY_LIST, day)
        self.select_date_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)

        input_date_after = input_date.get_attribute('value')
        return input_date_before, input_date_after

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_value(self):
        value_before = self.element_is_present(locator=self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')
        self.element_is_visible(locator=self.locators.START_BUTTON).click()
        time.sleep(2)
        value_after = self.element_is_present(locator=self.locators.PROGRESS_BAR).get_attribute('aria-valuenow')
        return value_before, value_after


class SliderBarPage(BasePage):
    locators = SliderBarPageLocators()

    def change_value(self):
        value_before = self.element_is_visible(locator=self.locators.SLIDER_VALUE).get_attribute('value')
        slider_bar = self.element_is_visible(locator=self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_bar, 10)
        value_after = self.element_is_visible(locator=self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def get_content(self, locator, locator2):
        self.element_is_visible(locator=locator).click()
        return self.element_is_visible(locator=locator2).text

    def check_tabs(self):
        what_content = self.get_content(self.locators.TABS_WHAT, self.locators.TABS_WHAT_CONTENT)
        origin_content = self.get_content(self.locators.TABS_ORIGIN, self.locators.TABS_ORIGIN_CONTENT)
        use_content = self.get_content(self.locators.TABS_USE, self.locators.TABS_USE_CONTENT)

        return what_content, origin_content, use_content


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tooltip(self, hover_elem, wait_elem):
        self.action_hover(hover_elem)
        self.element_is_visible(wait_elem)
        text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS).text
        self.action_hover(self.locators.HEADER)
        return text

    def check_tooltips(self):
        text = self.get_text_from_tooltip(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
        text2 = self.get_text_from_tooltip(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
        text3 = self.get_text_from_tooltip(self.locators.CONTRARY_LINK, self.locators.TOOL_TIP_CONTRARY)
        text4 = self.get_text_from_tooltip(self.locators.SECTION_LINK, self.locators.TOOL_TIP_SECTION)
        return text, text2, text3, text4


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_items = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_items:
            self.action_hover(item, False)
            data.append(item.text)
        return data
