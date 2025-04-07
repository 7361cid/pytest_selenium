from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.XPATH, '//*[@id="userName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//*[@id="submit"]')

    CREATED_FULL_NAME = (By.XPATH, '//*[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//*[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')

    CHECKBOX_DESKTOP = (By.XPATH, '//*[@id="tree-node-desktop"]')
    CHECKBOX_NOTES = (By.XPATH, '//*[@id="tree-node-notes"]')
    CHECKBOX_COMMANDS = (By.XPATH, '//*[@id="tree-node-commands"]')
    CHECKBOX_DOCUMENTS = (By.XPATH, '//*[@id="tree-node-documents"]')
    CHECKBOX_WORKSPACE = (By.XPATH, '//*[@id="tree-node-workspace"]')
    CHECKBOX_REACT = (By.XPATH, '//*[@id="tree-node-react"]')
    CHECKBOX_ANGULAR = (By.XPATH, '//*[@id="tree-node-angular"]')
    CHECKBOX_PUBLIC = (By.XPATH, '//*[@id="tree-node-public"]')
    CHECKBOX_WORD_FILE = (By.XPATH, '//*[@id="tree-node-wordFile"]')


class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    RESULT = (By.XPATH, '//span[@class="text-success"]')

class TablePageLocators:
    ADD_BUTTON = (By.XPATH, '//button[@id="addNewRecordButton"]')
    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    EMAIL_NAME = (By.XPATH, '//*[@id="userEmail"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastName"]')
    AGE = (By.XPATH, '//*[@id="age"]')
    SALARY = (By.XPATH, '//*[@id="salary"]')
    DEPARTMENT = (By.XPATH, '//*[@id="department"]')
    SUBMIT = (By.XPATH, '//*[@id="submit"]')
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tbody"]')
    TABLE_ROW = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH = (By.XPATH, '//*[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    RESULT = (By.XPATH, '//div[@class="rt-noData"]')
    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')
    TABLE_ITEM = ".//ancestor::div[@class='rt-tr-group']"
    PAGE_COUNT_SELECT = (By.XPATH, '//select[@aria-label="rows per page"]')

class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.XPATH, '//*[@id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.XPATH, '//*[@id="rightClickBtn"]')
    CLICK_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    DOUBLE_CLICK_TEXT = (By.XPATH, '//*[@id="doubleClickMessage"]')
    RIGHT_CLICK_TEXT = (By.XPATH, '//*[@id="rightClickMessage"]')
    CLICK_TEXT = (By.XPATH, '//*[@id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, '//*[@id="simpleLink"]')
    DYNAMIC_LINK = (By.XPATH, '//*[@id="dynamicLink"]')
    CREATED_LINK = (By.XPATH, '//*[@id="created"]')
    NO_CONTENT_LINK = (By.XPATH, '//*[@id="no-content"]')
    MOVED_LINK = (By.XPATH, '//*[@id="moved"]')
    BAD_REQUEST_LINK = (By.XPATH, '//*[@id="bad-request"]')
    UNAUTHORIZED_LINK = (By.XPATH, '//*[@id="unauthorized"]')

class DownloadPageLocators:
    DOWNLOAD_URL = (By.XPATH, '//*[@id="downloadButton"]')
    UPLOAD_INPUT = (By.XPATH, '//*[@id="uploadFile"]')
    FILE_TEXT = (By.XPATH, '//*[@id="uploadedFilePath"]')
