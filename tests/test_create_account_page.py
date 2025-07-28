import allure
from pages.create_account_page import CreateAccountPage


@allure.feature('Тесты на создание аккаунта')
class TestCreateAccountPage:

    @allure.title('Проверка отображения страницы авторизации после создания аккаунта')
    def test_is_sign_in_page_opened_after_create_account(self, driver):
        create_page = CreateAccountPage(driver)
        create_page.create_account()

        assert create_page.is_sign_in_page_opened()

    @allure.title('Проверка отображения формы регистрации после создания аккаунта')
    def test_is_sign_in_form_displayed_after_create_account(self, driver):
        create_page = CreateAccountPage(driver)
        create_page.create_account()

        assert create_page.is_sign_in_form_displayed()
