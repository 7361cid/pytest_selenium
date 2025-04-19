import time

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderBarPage,\
    TabsPage, ToolTipsPage, MenuPage


class TestWidget:
    # class TestWindowsPage:
    #     def test_accordian_page(self, driver):
    #         page = AccordianPage(driver, "https://demoqa.com/accordian")
    #         page.open()
    #         texts = page.check_accordian()
    #         assert texts[0] == "What is Lorem Ipsum?"
    #         assert len(texts[1]) == 574
    #         assert texts[2] == "Where does it come from?"
    #         assert len(texts[3]) == 1059
    #         assert texts[4] == "Why do we use it?"
    #         assert len(texts[5]) == 613

    #class TestAutoCompletePage:
        # def test_autocomplete_page(self, driver):
        #     page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        #     page.open()
        #     colors = page.fill_input_multi()
        #     count, count2 = page.delete_from_multi_input()
        #     colors2 = page.get_multi_input_values()
        #     assert count == 3
        #     assert count2 == 2
        #     for c in colors2:
        #         assert c in colors

        # def test_single_autocomplete(self, driver):
        #     page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        #     page.open()
        #     color = page.fill_input_single()
        #     color2 = page.check_single_color()
        #     assert color == color2
    # class TestDatePicker:
    #      def test_choose_date(self, driver):
    #          page = DatePickerPage(driver, "https://demoqa.com/date-picker")
    #          page.open()
    #          date_before, date_after = page.select_date()
    #          assert date_before != date_after
    #
    #     def test_choose_date_and_time(self, driver):
    #         page = DatePickerPage(driver, "https://demoqa.com/date-picker")
    #         page.open()
    #         date_before, date_after = page.select_date_and_time()
    #         assert date_before != date_after

    # class TestProgressBar:
    #     def test_progress_bar(self, driver):
    #         page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
    #         page.open()
    #         val, val2 = page.change_value()
    #         assert val < val2

    # class TestSliderBar:
    #     def test_slider_bar(self, driver):
    #         page = SliderBarPage(driver, "https://demoqa.com/slider")
    #         page.open()
    #         val, val2 = page.change_value()
    #         assert val < val2

    # class TestTabs:
    #     def test_tabs(self, driver):
    #         page = TabsPage(driver, "https://demoqa.com/tabs")
    #         page.open()
    #         data = page.check_tabs()
    #         assert len(data[0]) == 574
    #         assert len(data[1]) == 1059
    #         assert len(data[2]) == 613

    # class TestTabs:
    #     def test_tabs(self, driver):
    #         page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
    #         page.open()
    #         data = page.check_tooltips()
    #         assert data[0] == "You hovered over the Button"
    #         assert data[1] == "You hovered over the text field"
    #         assert data[2] == "You hovered over the Contrary"
    #         assert data[3] == "You hovered over the 1.10.32"

    class TestMenu:
        def test_menu(self, driver):
            page = MenuPage(driver, "https://demoqa.com/menu#")
            page.open()
            data = page.check_menu()
            assert data[0] == "Main Item 1"
            assert data[1] == "Main Item 2"
            assert data[2] == "Sub Item"
            assert data[3] == "Sub Item"
            assert data[4] == "SUB SUB LIST »"
            assert data[5] == "Sub Sub Item 1"
            assert data[6] == "Sub Sub Item 2"
            assert data[7] == "Main Item 3"