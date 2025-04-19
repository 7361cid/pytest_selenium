from selenium.webdriver.common.by import By


class WindowsPageLocators:
    TAB_BUTTON = (By.XPATH, '//*[@id="tabButton"]')
    TAB_TEXT = (By.XPATH, '//*[@id="sampleHeading"]')
    WINDOW_BUTTON = (By.XPATH, '//*[@id="windowButton"]')


class AlertsPageLocators:
    ALERT_BUTTON = (By.XPATH, '//*[@id="alertButton"]')
    ALERT_TIMER_BUTTON = (By.XPATH, '//*[@id="timerAlertButton"]')
    ALERT_PROMT_BUTTON = (By.XPATH, '//*[@id="promtButton"]')
    ALERT_CONFIRM_BUTTON = (By.XPATH, '//*[@id="confirmButton"]')
    CONFIRM_TEXT = (By.XPATH, '//*[@id="confirmResult"]')
    PROMT_TEXT = (By.XPATH, '//*[@id="promptResult"]')


class FramePageLocators:
    FIRST_FRAME = (By.XPATH, '//*[@id="frame1"]')
    SECOND_FRAME = (By.XPATH, '//*[@id="frame2"]')
    FRAME_TEXT = (By.XPATH, '//*[@id="sampleHeading"]')


class NestedFramePageLocators:
    FIRST_FRAME = (By.XPATH, '//*[@id="frame1"]')
    SECOND_FRAME = (By.XPATH, '//*[@srcdoc="<p>Child Iframe</p>"]')
    FRAME_TEXT = (By.XPATH, '//body')
    SECOND_FRAME_TEXT = (By.XPATH, '//p')


class ModalDialogPageLocators:
    SMALL_MODAL = (By.XPATH, '//*[@id="showSmallModal"]')
    SMALL_MODAL_CLOSE = (By.XPATH, '//*[@id="closeSmallModal"]')
    BIG_MODAL = (By.XPATH, '//*[@id="showLargeModal"]')
    BIG_MODAL_CLOSE = (By.XPATH, '//*[@id="closeLargeModal"]')
    BODY_TEXT = (By.XPATH, '//div[@class="modal-body"]')
    TITLE = (By.XPATH, '//*[@id="example-modal-sizes-title-sm"]')
    TITLE_BIG = (By.XPATH, '//*[@id="example-modal-sizes-title-lg"]')
