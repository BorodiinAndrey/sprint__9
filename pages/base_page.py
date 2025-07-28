import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=timeout)

    @allure.step("Клик на элемент")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста в поле")
    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
        element.send_keys(text)

    @allure.step("Ввод текста в поле из списка локаторов")
    def enter_text_from_list(self, locator, text, index):
        elements = self.wait.until(EC.visibility_of_all_elements_located(locator))
        elements[index].click()
        elements[index].send_keys(text)

    @allure.step("Получение текущей ссылки")
    def get_current_link(self, url=None):
        self.wait.until(EC.url_contains(url))
        return self.driver.current_url

    @allure.step("Проверка отображения элемента")
    def check_displaying_of_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    @allure.step("Получение текста")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
