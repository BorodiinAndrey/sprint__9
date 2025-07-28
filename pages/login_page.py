import allure
from data.urls import RECIPES_URL
from locators.base_page_locators import EMAIL_FIELD_LOCATOR, PASSWORD_FIELD_LOCATOR, ENTER_BUTTON_LOCATOR
from locators.create_account_page_locators import SIGN_IN_FORM_LOCATOR
from locators.login_page_locators import EXIT_BUTTON_LOCATOR
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login_user(self, email, password):
        self.check_displaying_of_element(SIGN_IN_FORM_LOCATOR)
        self.enter_text(EMAIL_FIELD_LOCATOR, email)
        self.enter_text(PASSWORD_FIELD_LOCATOR, password)
        self.click_element(ENTER_BUTTON_LOCATOR)

    @allure.step("Проверка открытия главной страницы")
    def is_main_page_opened(self):
        return self.get_current_link(RECIPES_URL) == RECIPES_URL

    @allure.step("Проверка отображения кнопки Выход")
    def is_exit_button_displayed(self):
        return self.check_displaying_of_element(EXIT_BUTTON_LOCATOR)
