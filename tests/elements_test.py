import time

from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, TablePage, ButtonsPage, \
    LinksPage, DownloadPage

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

   # class TestTable:
        # def test_add_person(self, driver):
        #     page = TablePage(driver, "https://demoqa.com/webtables")
        #     page.open()
        #     input = page.add_new_person()
        #     output = page.check_new_added_person()
        #     assert input in output

        # def test_table_search(self, driver):
        #     page = TablePage(driver, "https://demoqa.com/webtables")
        #     page.open()
        #     input = page.add_new_person()
        #     page.search(input[0])
        #     output = page.check_search()
        #     assert input == output

        # def test_edit_person(self, driver):
        #     page = TablePage(driver, "https://demoqa.com/webtables")
        #     page.open()
        #     input = page.add_new_person()
        #     page.search(input[0])
        #     age = page.update_person_info()
        #     output = page.check_search()
        #     assert age in output

        # def test_delete_person(self, driver):
        #     page = TablePage(driver, "https://demoqa.com/webtables")
        #     page.open()
        #     input = page.add_new_person()
        #     page.search(input[0])
        #     page.delete_person()
        #     text = page.check_deleted()
        #     assert text == "No rows found"
        # def test_count_row(self, driver):
        #     page = TablePage(driver, "https://demoqa.com/webtables")
        #     page.open()
        #     page.select_rows_count()
        #     rows_count = page.get_rows_count()
        #     assert rows_count == 25
    # class TestButtons:
    #     def test_buttons_click(self, driver):
    #         page = ButtonsPage(driver, "https://demoqa.com/buttons")
    #         page.open()
    #         texts = page.click_buttons()
    #         assert texts[0] == "You have done a dynamic click"
    #         assert texts[1] == "You have done a double click"
    #         assert texts[2] == "You have done a right click"

    # class TestLinks:
    #     def test_check_link(self, driver):
    #         page = LinksPage(driver, "https://demoqa.com/links")
    #         page.open()
    #         element_link, current_url = page.click_new_tab_simlpe_link()
    #         print(element_link, current_url)
    #         assert element_link == "https://demoqa.com/"
    #         assert current_url == "https://demoqa.com/"
    #
    #     def test_broken_link(self, driver):
    #         page = LinksPage(driver, "https://demoqa.com/links")
    #         page.open()
    #         response_code = page.check_broken_link("https://demoqa.com/bad-request")
    #         assert response_code == 400

    class TestDownload:
        def test_download_file(self, driver):
            page = DownloadPage(driver, "https://demoqa.com/upload-download")
            page.open()
            page.download_file()