import time

from pages.base_page import BasePage
from locators.alerts_page_locators import WindowsPageLocators, AlertsPageLocators, FramePageLocators,\
    NestedFramePageLocators, ModalDialogPageLocators


class WindowsPage(BasePage):
    locators = WindowsPageLocators()

    def shared_steps(self):
        self.switch_to_new_tab(1)
        text = self.element_is_visible(locator=self.locators.TAB_TEXT).text
        url = self.driver.current_url
        return text, url

    def open_new_tab(self):
        self.element_is_visible(locator=self.locators.TAB_BUTTON).click()
        return self.shared_steps()

    def open_new_window(self):
        self.element_is_visible(locator=self.locators.WINDOW_BUTTON).click()
        return self.shared_steps()


class AletrsPage(BasePage):
    locators = AlertsPageLocators

    def check_see_alert(self):
        self.element_is_visible(locator=self.locators.ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        text = alert_window.text
        return text

    def check_alert_timer(self):
        self.element_is_visible(locator=self.locators.ALERT_TIMER_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        text = alert_window.text
        return text

    def check_confirm_alert(self):
        self.element_is_visible(locator=self.locators.ALERT_CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        return self.element_is_visible(locator=self.locators.CONFIRM_TEXT).text

    def check_confirm_alert_promt(self):
        self.element_is_visible(locator=self.locators.ALERT_PROMT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys("alert_text")
        alert_window.accept()
        return self.element_is_visible(locator=self.locators.PROMT_TEXT).text


class FramePage(BasePage):
    locators = FramePageLocators

    def check_frame(self):
        frame = self.element_is_present(locator=self.locators.FIRST_FRAME)
        height = frame.get_attribute('height')
        width = frame.get_attribute('width')

        frame2 = self.element_is_present(locator=self.locators.SECOND_FRAME)
        height2 = frame2.get_attribute('height')
        width2 = frame2.get_attribute('width')

        self.driver.switch_to.frame(frame)
        text = self.element_is_present(locator=self.locators.FRAME_TEXT).text
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(frame2)
        text2 = self.element_is_present(locator=self.locators.FRAME_TEXT).text

        return height, width, height2, width2, text, text2


class NestedFramePage(BasePage):
    locators = NestedFramePageLocators

    def get_frame_text(self, locator_frame, locator_text):
        frame = self.element_is_present(locator=locator_frame)
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(locator=locator_text).text
        return text

    def check_nested_frames(self):
        text = self.get_frame_text(self.locators.FIRST_FRAME, self.locators.FRAME_TEXT)
        text2 = self.get_frame_text(self.locators.SECOND_FRAME, self.locators.SECOND_FRAME_TEXT)
        return text, text2


class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators

    def check_modal_dialogs(self):
        self.element_is_visible(locator=self.locators.SMALL_MODAL).click()
        title = self.element_is_visible(locator=self.locators.TITLE).text
        text = self.element_is_visible(locator=self.locators.BODY_TEXT).text
        self.element_is_visible(locator=self.locators.SMALL_MODAL_CLOSE).click()

        self.element_is_visible(locator=self.locators.BIG_MODAL).click()
        title2 = self.element_is_visible(locator=self.locators.TITLE_BIG).text
        text2 = self.element_is_visible(locator=self.locators.BODY_TEXT).text
        self.element_is_visible(locator=self.locators.BIG_MODAL_CLOSE).click()
        return title, text, title2, text2