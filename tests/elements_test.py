import time
import allure

from pages.elements_page import TextBoxPage, CheckboxPage, RadioButtonPage, TablePage, ButtonsPage, \
    LinksPage, DownloadPage, DynamicElementsPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_textbox_elements(self, driver):
            page = TextBoxPage(driver, "https://demoqa.com/text-box")
            page.open()
            input_name, input_email, input_address, input_permanent_address = page.fill_all_fields()
            output_name, output_email, output_address, output_permanent_address = page.check_filled_form()
            assert output_name == input_name
            assert output_email == input_email
            assert output_address == input_address
            assert output_permanent_address == input_permanent_address

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_open_full_list(self, driver):
            page = CheckboxPage(driver, "https://demoqa.com/checkbox")
            page.open()
            page.open_full_list()
            page.click_random_checkbox()
            input = page.get_checked_items()
            output = page.get_output_result()
            assert input == output

    @allure.feature("RadioButton")
    class TestRadioButton:
        @allure.title("Check RadioButton")
        def test_radiobutton(self, driver):
            page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            page.open()
            page.click_radio_button("yes")
            results = page.get_output_result()
            page.click_radio_button("impressive")
            results2 = page.get_output_result()
            page.click_radio_button("no")
            results3 = page.get_output_result()
            assert results == "Yes", "Results not equal yes"
            assert results2 == "Impressive", "Results not equal impressive"
            assert results3 == "Impressive", "Results not equal impressive"

    @allure.feature("Table")
    class TestTable:
        @allure.title("Check Table")
        def test_add_person(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
            input = page.add_new_person()
            output = page.check_new_added_person()
            assert input in output

        @allure.title("Check Table Search")
        def test_table_search(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
            input = page.add_new_person()
            page.search(input[0])
            output = page.check_search()
            assert input == output

        @allure.title("Check Table Edit")
        def test_edit_person(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
            input = page.add_new_person()
            page.search(input[0])
            age = page.update_person_info()
            output = page.check_search()
            assert age in output

        @allure.title("Check TableDelete")
        def test_delete_person(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
            input = page.add_new_person()
            page.search(input[0])
            page.delete_person()
            text = page.check_deleted()
            assert text == "No rows found"

        @allure.title("Check Count Rows")
        def test_count_row(self, driver):
            page = TablePage(driver, "https://demoqa.com/webtables")
            page.open()
            page.select_rows_count()
            rows_count = page.get_rows_count()
            assert rows_count == 25

    @allure.feature("Buttons")
    class TestButtons:
        @allure.title("Check Buttons Click")
        def test_buttons_click(self, driver):
            page = ButtonsPage(driver, "https://demoqa.com/buttons")
            page.open()
            texts = page.click_buttons()
            assert texts[0] == "You have done a dynamic click"
            assert texts[1] == "You have done a double click"
            assert texts[2] == "You have done a right click"

    @allure.feature("Links")
    class TestLinks:
        @allure.title("Check Link")
        def test_check_link(self, driver):
            page = LinksPage(driver, "https://demoqa.com/links")
            page.open()
            element_link, current_url = page.click_new_tab_simlpe_link()
            print(element_link, current_url)
            assert element_link == "https://demoqa.com/"
            assert current_url == "https://demoqa.com/"

        @allure.title("Check Broken Link")
        def test_broken_link(self, driver):
            page = LinksPage(driver, "https://demoqa.com/links")
            page.open()
            response_code = page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400

    @allure.feature("DownloadFiles")
    class TestDownload:
        @allure.title("Check Download File")
        def test_download_file(self, driver):
            page = DownloadPage(driver, "https://demoqa.com/upload-download")
            page.open()
            image_type = page.download_file()
            assert image_type == "jpeg"

        @allure.title("Check Upload File")
        def test_upload_file(self, driver):
            page = DownloadPage(driver, "https://demoqa.com/upload-download")
            page.open()
            path = page.upload_file()
            assert path == "C:\\fakepath\\text.txt"

    @allure.feature("DynamicElements")
    class TestDynamicElements:
        @allure.title("Check Dynamic Elements")
        def test_dynamic_elements(self, driver):
            page = DynamicElementsPage(driver, "https://demoqa.com/dynamic-properties")
            page.open()
            css_before, css_after, count = page.check_changed_color()
            assert str(css_after) == "rgba(220, 53, 69, 1)"
            assert str(css_before) == "rgba(255, 255, 255, 1)"
            assert count == 5
