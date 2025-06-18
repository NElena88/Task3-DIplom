import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from seletools.actions import drag_and_drop
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Скролл до конца страницы")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Получаем текст элемента через JS')
    def get_element_text_js(self, locator):
        return self.driver.execute_script("return arguments[0].textContent;", self.driver.find_element(*locator))

    @allure.step('Ожидаем изменения текста')
    def wait_for_text_change(self, locator, initial_text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_element_text_js(locator) != initial_text
        )

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=15):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=15):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Подождать изменение текста элемента')
    def wait_text_element_to_change(self, test_locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(test_locator, value))

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Подождать, пока элемент перестанет существовать или станет невидимым")
    def wait_until_not_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Подождать появления /account/profile в url")
    def wait_url(self, url_substring, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_substring))

    @allure.step("Подождать кликабельности элемента")
    def wait_for_clickable_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step('Найти элемент')
    def find_element(self, locator, timeout=None):
        return self.wait_for_element(locator, timeout) if timeout else self.driver.find_element(*locator)