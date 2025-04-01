import time

from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_textbox_elements(self, driver):
            page = TextBoxPage(driver, "http://demoqa.com/text-box")
            page.open()
            input_name, input_email, input_address, input_permanent_address = page.fill_all_fields()
            output_name, output_email, output_address, output_permanent_address = page.check_filled_form()
            assert output_name == input_name
            assert output_email == input_email
            assert output_address == input_address
            assert output_permanent_address == input_permanent_address

