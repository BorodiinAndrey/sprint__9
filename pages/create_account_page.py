import allure
from data.urls import SIGN_IN_URL
from helper.helper_user import create_fake_email, create_fake_password, create_fake_first_name, create_fake_last_name, create_fake_user_name
from locators.base_page_locators import CREATE_ACCOUNT_BUTTON_ON_MAIN_PAGE_LOCATOR, FIRST_NAME_FIELD_LOCATOR, LAST_NAME_FIELD_LOCATOR, \
    USER_NAME_FIELD_LOCATOR, EMAIL_FIELD_LOCATOR, PASSWORD_FIELD_LOCATOR, CREATE_ACCOUNT_BUTTON_ON_REGISTRATION_LOCATOR
from locators.create_account_page_locators import SIGN_IN_FORM_LOCATOR
from pages.base_page import BasePage


class CreateAccountPage(BasePage):

    @allure.step("Создание аккаунта")
    def create_account(self):

        email = create_fake_email()
        password = create_fake_password()

        self.click_element(CREATE_ACCOUNT_BUTTON_ON_MAIN_PAGE_LOCATOR)
        self.enter_text(FIRST_NAME_FIELD_LOCATOR, create_fake_first_name())
        self.enter_text(LAST_NAME_FIELD_LOCATOR, create_fake_last_name())
        self.enter_text(USER_NAME_FIELD_LOCATOR, create_fake_user_name())
        self.enter_text(EMAIL_FIELD_LOCATOR, email)
        self.enter_text(PASSWORD_FIELD_LOCATOR, password)
        self.click_element(CREATE_ACCOUNT_BUTTON_ON_REGISTRATION_LOCATOR)

        return {
            "email": email,
            "password": password
        }

    @allure.step("Проверка открытия страницы логина")
    def is_sign_in_page_opened(self):
        return self.get_current_link(SIGN_IN_URL) == SIGN_IN_URL

    @allure.step("Проверка отображения формы логина")
    def is_sign_in_form_displayed(self):
        return self.check_displaying_of_element(SIGN_IN_FORM_LOCATOR)
