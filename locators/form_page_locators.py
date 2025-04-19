from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.XPATH, '//*[@id="firstName"]')
    LAST_NAME = (By.XPATH, '//*[@id="lastName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    GENDER_MALE = (By.XPATH, '//label[@for="gender-radio-1"]')
    GENDER_FEMALE = (By.XPATH, '//label[@for="gender-radio-2"]')
    PHONE_NUMBER = (By.XPATH, '//*[@id="userNumber"]')
    BDAY = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    SUBJECTS = (By.XPATH, '//*[@id="subjectsInput"]')
    HOBBY_SPORTS = (By.XPATH, '//label[@for="hobbies-checkbox-1"]')
    HOBBY_READING = (By.XPATH, '//label[@for="hobbies-checkbox-2"]')
    HOBBY_MUSIC = (By.XPATH, '//label[@for="hobbies-checkbox-3"]')
    PICTURE = (By.XPATH, '//*[@id="uploadPicture"]')
    ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    STATE_SELECT = (By.XPATH, '//div[@id="state"]')
    STATE_INPUT = (By.XPATH, '//*[@id="react-select-3-input"]')
    CITY_INPUT = (By.XPATH, '//*[@id="react-select-4-input"]')
    CITY_SELECT = (By.XPATH, '//div[@id="city"]')
    SUBMIT = (By.XPATH, '//*[@id="submit"]')

    TABLE_NAME = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[1]/td[2]')
    TABLE_EMAIL = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[2]/td[2]')
    TABLE_GENDER = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[3]/td[2]')
    TABLE_PHONE = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[4]/td[2]')
    TABLE_BDAY = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[5]/td[2]')
    TABLE_SUBJECTS = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[6]/td[2]')
    TABLE_HOBBIES = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[7]/td[2]')
    TABLE_PICTURE = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[8]/td[2]')
    TABLE_ADDRESS = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[9]/td[2]')
    TABLE_STATE = (
    By.XPATH, '//table[@class="table table-dark table-striped table-bordered table-hover"]/tbody/tr[10]/td[2]')

# 91/3095 от 11.03
