from pages.alerts_page import WindowsPage, AletrsPage, FramePage, NestedFramePage, ModalDialogPage


class TestAlerts:
    class TestWindowsPage:
        def test_new_tab(self, driver):
            page = WindowsPage(driver, "https://demoqa.com/browser-windows")
            page.open()
            text, url = page.open_new_tab()
            assert text == "This is a sample page"
            assert url == "https://demoqa.com/sample"

        def test_new_widnow(self, driver):
            page = WindowsPage(driver, "https://demoqa.com/browser-windows")
            page.open()
            text, url = page.open_new_window()
            assert text == "This is a sample page"
            assert url == "https://demoqa.com/sample"

    class TestAlertsPage:
        def test_see_alert(self, driver):
            page = AletrsPage(driver, "https://demoqa.com/alerts")
            page.open()
            text = page.check_see_alert()
            assert text == "You clicked a button"

        def test_timer_alert(self, driver):
            page = AletrsPage(driver, "https://demoqa.com/alerts")
            page.open()
            text = page.check_alert_timer()
            assert text == "This alert appeared after 5 seconds"

        def test_confirm_alert(self, driver):
            page = AletrsPage(driver, "https://demoqa.com/alerts")
            page.open()
            text = page.check_confirm_alert()
            assert text == "You selected Ok"

        def test_alert_with_promt(self, driver):
            page = AletrsPage(driver, "https://demoqa.com/alerts")
            page.open()
            text = page.check_confirm_alert_promt()
            assert text == "You entered alert_text"
    class TestFramePage:
        def test_frame(self, driver):
            page = FramePage(driver, "https://demoqa.com/frames")
            page.open()
            h, w, h2, w2, text, text2 = page.check_frame()
            assert h == "350px"
            assert w == "500px"
            assert h2 == "100px"
            assert w2 == "100px"
            assert text == "This is a sample page"
            assert text2 == "This is a sample page"

    class TestNestedFramePage:
        def test_frame(self, driver):
             page = NestedFramePage(driver, "https://demoqa.com/nestedframes")
             page.open()
             text, text2 = page.check_nested_frames()
             assert text == "Parent frame"
             assert text2 == "Child Iframe"

    class TestModalDialogPage:
        def test_modal_dialog(self, driver):
            page = ModalDialogPage(driver, "https://demoqa.com/modal-dialogs")
            page.open()
            data = page.check_modal_dialogs()
            print(data)
            assert data[0] == "Small Modal"
            assert data[1] == "This is a small modal. It has very less content"
            assert data[2] == "Large Modal"
            assert len(data[3]) == 574