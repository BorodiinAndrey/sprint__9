from selenium.webdriver.common.by import By


CREATE_RECIPE_BUTTON_LOCATOR = [By.XPATH, "//a[text()='Создать рецепт']"]
RECIPE_NAME_OR_TIME_FOR_READY_FIELDS_LOCATOR = [By.XPATH, "//input[@class='styles_inputField__3eqTj']"]
INGREDIENT_LOCATOR = [By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsInput__1zzql']"]
CHOOSE_INGREDIENT_LOCATOR = [By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]//div[text()='фазан']"]
WEIGHT_LOCATOR = [By.XPATH, "//input[@class='styles_inputField__3eqTj styles_ingredientsAmountValue__2matT']"]
ADD_INGREDIENT_LOCATOR = [By.XPATH, "//div[text()='Добавить ингредиент']"]
DESCRIPTION_FIELD_LOCATOR = [By.XPATH, "//*[@class='styles_textareaField__1wfhC']"]
PHOTO_INPUT_LOCATOR = [By.XPATH, "//input[@type='file']"]
CREATE_RECIPE_BUTTON_FORM_LOCATOR = [By.XPATH, "//button[text()='Создать рецепт']"]
RECIPE_CARD_LOCATOR = [By.XPATH, "//div[@class='styles_single-card__1yTTj']"]
RECIPE_NAME_CARD_LOCATOR = [By.XPATH, "//h1[@class='styles_single-card__title__2QMPq']"]
