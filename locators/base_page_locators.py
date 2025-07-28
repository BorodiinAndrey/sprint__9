from selenium.webdriver.common.by import By


CREATE_ACCOUNT_BUTTON_ON_MAIN_PAGE_LOCATOR = [By.XPATH, "//a[text()='Создать аккаунт']"]
FIRST_NAME_FIELD_LOCATOR = [By.XPATH, "//input[@name='first_name']"]
LAST_NAME_FIELD_LOCATOR = [By.XPATH, "//input[@name='last_name']"]
USER_NAME_FIELD_LOCATOR = [By.XPATH, "//input[@name='username']"]
EMAIL_FIELD_LOCATOR = [By.XPATH, "//input[@name='email']"]
PASSWORD_FIELD_LOCATOR = [By.XPATH, "//input[@name='password']"]
CREATE_ACCOUNT_BUTTON_ON_REGISTRATION_LOCATOR = [By.XPATH, "//button[text()='Создать аккаунт']"]
ENTER_BUTTON_LOCATOR = [By.XPATH, "//button[text()='Войти']"]