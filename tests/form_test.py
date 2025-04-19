from pages.form_page import FormPage


class TestForm:
    class TestPersonForm:
        def test_textbox_elements(self, driver):
            page = FormPage(driver, "https://demoqa.com/automation-practice-form")
            page.open()
            fields_data = page.fill_all_fields()
            table_data = page.get_data_from_table()
            assert table_data[0] == f"{fields_data[0]} {fields_data[1]}"
            assert table_data[1] == fields_data[2]
            assert table_data[2] == fields_data[3]
            assert table_data[3] == fields_data[4][:10]
            assert table_data[4] == fields_data[6]
            assert table_data[5] == 'Maths'
            assert table_data[6] == fields_data[5]
            assert table_data[7] == 'text.txt'
            assert table_data[8] == fields_data[7]
            assert table_data[9] == 'NCR Delhi'
