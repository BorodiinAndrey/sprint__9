import allure
from pages.create_account_page import CreateAccountPage
from pages.login_page import LoginPage


@allure.feature('Тесты на логин')
class TestLoginPage:

    @allure.title('Проверка отображения страницы авторизации после создания аккаунта')
    def test_is_sign_in_page_opened_after_create_account(self, driver):
        create_page = CreateAccountPage(driver)
        creds = create_page.create_account()

        login_page = LoginPage(driver)
        login_page.login_user(creds["email"], creds["password"])

        assert login_page.is_main_page_opened()

    @allure.title('Проверка отображения формы регистрации после создания аккаунта')
    def test_is_sign_in_form_displayed_after_create_account(self, driver):
        create_page = CreateAccountPage(driver)
        creds = create_page.create_account()

        login_page = LoginPage(driver)
        login_page.login_user(creds["email"], creds["password"])

        assert login_page.is_exit_button_displayed()
