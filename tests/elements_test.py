import time

from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, TablePage

class TestElements:

    #class TestTextBox:
        # def test_textbox_elements(self, driver):
        #     page = TextBoxPage(driver, "https://demoqa.com/text-box")
        #     page.open()
        #     input_name, input_email, input_address, input_permanent_address = page.fill_all_fields()
        #     output_name, output_email, output_address, output_permanent_address = page.check_filled_form()
        #     assert output_name == input_name
        #     assert output_email == input_email
        #     assert output_address == input_address
        #     assert output_permanent_address == input_permanent_address

    # class TestCheckBox:
    #     def test_open_full_list(self, driver):
    #         page = CheckboxPage(driver, "https://demoqa.com/checkbox")
    #         page.open()
    #         page.open_full_list()
    #         page.click_random_checkbox()
    #         input = page.get_checked_items()
    #         output = page.get_output_result()
    #         assert input == output

    # class TestRadioButton:
    #     def test_radiobutton(self, driver):
    #         page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
    #         page.open()
    #         page.click_radio_button("yes")
    #         results = page.get_output_result()
    #         page.click_radio_button("impressive")
    #         results2 = page.get_output_result()
    #         page.click_radio_button("no")
    #         results3 = page.get_output_result()
    #         assert results == "Yes", "Results not equal yes"
    #         assert results2 == "Impressive", "Results not equal impressive"
    #         assert results3 == "Impressive", "Results not equal impressive"

    class TestTable:
        def test_add_person(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
