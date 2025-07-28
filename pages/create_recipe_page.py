from pathlib import Path
import allure
from selenium.webdriver.support import expected_conditions as EC
from data.recipe_data import RECIPE_NAME, INGREDIENT, TIME_FOR_READY, WEIGHT, RECIPE_DESCRIPTION
from locators.create_recipe_page_locators import CREATE_RECIPE_BUTTON_LOCATOR, RECIPE_NAME_OR_TIME_FOR_READY_FIELDS_LOCATOR, INGREDIENT_LOCATOR, \
    CHOOSE_INGREDIENT_LOCATOR, WEIGHT_LOCATOR, ADD_INGREDIENT_LOCATOR, DESCRIPTION_FIELD_LOCATOR, PHOTO_INPUT_LOCATOR, \
    CREATE_RECIPE_BUTTON_FORM_LOCATOR, RECIPE_CARD_LOCATOR, RECIPE_NAME_CARD_LOCATOR
from pages.base_page import BasePage


class CreateRecipePage(BasePage):

    @allure.step("Загрузка фото рецепта")
    def upload_photo(self, filename):
        project_root = Path(__file__).parent.parent
        file_path = project_root / "assets" / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Не нашел файл загрузки: {file_path}")

        abs_path = str(file_path.resolve())
        input_el = self.wait.until(EC.presence_of_element_located(PHOTO_INPUT_LOCATOR))
        input_el.send_keys(abs_path)

    @allure.step('Создание рецепта')
    def create_recipe(self):
        self.click_element(CREATE_RECIPE_BUTTON_LOCATOR)
        self.enter_text_from_list(RECIPE_NAME_OR_TIME_FOR_READY_FIELDS_LOCATOR, RECIPE_NAME, 0)
        self.enter_text(INGREDIENT_LOCATOR, INGREDIENT)
        self.click_element(CHOOSE_INGREDIENT_LOCATOR)
        self.enter_text(WEIGHT_LOCATOR, WEIGHT)
        self.click_element(ADD_INGREDIENT_LOCATOR)
        self.enter_text_from_list(RECIPE_NAME_OR_TIME_FOR_READY_FIELDS_LOCATOR, TIME_FOR_READY, 1)
        self.enter_text(DESCRIPTION_FIELD_LOCATOR, RECIPE_DESCRIPTION)
        self.upload_photo("image.jpg")
        self.click_element(CREATE_RECIPE_BUTTON_FORM_LOCATOR)

    @allure.step('Проверка отображения карточки рецепта')
    def is_recipe_card_displayed(self):
        return self.check_displaying_of_element(RECIPE_CARD_LOCATOR)

    @allure.step('Проверка отображения корректного имени карточки рецепта')
    def is_recipe_name_true(self):
        return self.get_text(RECIPE_NAME_CARD_LOCATOR) == RECIPE_NAME
