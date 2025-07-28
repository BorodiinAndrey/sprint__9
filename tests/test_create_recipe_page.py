import allure
from pages.create_account_page import CreateAccountPage
from pages.create_recipe_page import CreateRecipePage
from pages.login_page import LoginPage


@allure.feature('Тесты на создание рецептов')
class TestCreateRecipePage:

    @allure.title('Проверка, что отображается карточка созданного рецепта')
    def test_is_recipe_card_displayed_after_creating(self, driver):
        create_page = CreateAccountPage(driver)
        creds = create_page.create_account()

        login_page = LoginPage(driver)
        login_page.login_user(creds["email"], creds["password"])

        create_recipe = CreateRecipePage(driver)
        create_recipe.create_recipe()

        assert create_recipe.is_recipe_card_displayed()

    @allure.title('Проверка, что отображается название рецепта, которое заполняли при создании')
    def test_is_recipe_name_displayed_after_creating(self, driver):
        create_page = CreateAccountPage(driver)
        creds = create_page.create_account()

        login_page = LoginPage(driver)
        login_page.login_user(creds["email"], creds["password"])

        create_recipe = CreateRecipePage(driver)
        create_recipe.create_recipe()

        assert create_recipe.is_recipe_name_true
