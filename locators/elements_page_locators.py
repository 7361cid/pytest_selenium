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
