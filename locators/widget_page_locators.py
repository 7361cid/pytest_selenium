from selenium.webdriver.common.by import By


class AccordianPageLocators:
    HEADER_1 = (By.XPATH, '//*[@id="section1Heading"]')
    TEXT_1 = (By.XPATH, '//*[@id="section1Content"]')

    HEADER_2 = (By.XPATH, '//*[@id="section2Heading"]')
    TEXT_2 = (By.XPATH, '//*[@id="section2Content"]')

    HEADER_3 = (By.XPATH, '//*[@id="section3Heading"]')
    TEXT_3 = (By.XPATH, '//*[@id="section3Content"]')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.XPATH, '//*[@id="autoCompleteMultipleInput"]')
    MULTI_INPUT_VALUES = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_INPUT = (By.XPATH, '//*[@id="autoCompleteSingleInput"]')
    SINGLE_INPUT_VALUE = (By.XPATH, '//div[@class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    SELECT_DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    SELECT_MONTH = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    SELECT_YEAR = (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    SELECT_DATE_AND_TIME_INPUT = (By.XPATH, '//*[@id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class ProgressBarPageLocators:
    START_BUTTON = (By.XPATH, '//*[@id="startStopButton"]')
    PROGRESS_BAR = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class SliderBarPageLocators:
    SLIDER_VALUE = (By.XPATH, '//*[@id="sliderValue"]')
    INPUT_SLIDER = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')


class TabsPageLocators:
    TABS_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')
    TABS_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')
    TABS_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK = (By.XPATH, '//*[.="Contrary"]')
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK = (By.XPATH, '//*[.="1.10.32"]')
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')
    HEADER = (By.XPATH, '//*[@id="toopTipContainer"]/h1')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')


