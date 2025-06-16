import allure

from locators.constructor_locators import ConstructorPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_until_not_visible(ConstructorPageLocators.OVERLAY)

    @allure.step('Кликаем на кнопку Конструктор')
    def click_button_constructor(self):
        self.click_on_element(ConstructorPageLocators.BTN_CONSTRUCTOR)

    @allure.step('Кликаем на кнопку Войти в аккаунт')
    def click_button_sign_in(self):
        self.click_on_element(ConstructorPageLocators.BTN_LOGIN_ACCOUNT)

    @allure.step('Ожидаем появления заголовка Соберите бургер')
    def wait_for_header_make_burger(self):
        self.wait_for_element(ConstructorPageLocators.HEADER_MAKE_BURGER)

    @allure.step('Получаем текст заголовка Соберите бургер')
    def get_make_burger_text(self):
        return self.get_text_on_element(ConstructorPageLocators.HEADER_MAKE_BURGER)

    @allure.step('Кликаем по ингредиенту булка')
    def click_on_ingredient_bun(self):
        self.click_on_element(ConstructorPageLocators.INGR_BUN)

    @allure.step('Ожидаем появления модального окна Детали ингредиента')
    def wait_for_header_popup(self):
        self.wait_for_element(ConstructorPageLocators.POPUP_HEADER_INGR)

    @allure.step('Получаем текст заголовка модального окна Детали ингредиента')
    def get_details_ingredient_text(self):
        return self.get_text_on_element(ConstructorPageLocators.POPUP_HEADER_INGR)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_popup_with_ingredient_details(self):
        self.click_on_element(ConstructorPageLocators.POPUP_CLOSE)

    @allure.step('Получаем число со счетчика ингредиента Соус')
    def get_count_ingredient_sauce(self):
        count = int(self.get_text_on_element(ConstructorPageLocators.COUNTER_INGR_SAUCE))
        return count

    @allure.step('Перетащить булки в конструктор')
    def drag_bun_to_constructor(self):
        source_bun = self.driver.find_element(*ConstructorPageLocators.INGR_BUN)
        target_bun = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR)
        self.drag_and_drop_element(source_bun, target_bun)

    @allure.step('Перетащить соус в конструктор')
    def drag_sauce_to_constructor(self):
        source_sauce = self.driver.find_element(*ConstructorPageLocators.INGR_SAUCE)
        target_sauce = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR)
        self.drag_and_drop_element(source_sauce, target_sauce)

    @allure.step('Ожидаем появления ингредиента Соус в конструкторе')
    def wait_ingredient_sauce_in_constructor(self):
        self.wait_for_element(ConstructorPageLocators.INGR_SAUCE_IN_CONST)

    @allure.step('Ожидаем появления кнопки Оформить заказ')
    def wait_button_create_order(self):
        self.wait_for_element(ConstructorPageLocators.CREATE_ORDER)

    @allure.step('Кликаем по кнопке Оформить заказ')
    def click_on_button_create_order(self):
        self.click_on_element(ConstructorPageLocators.CREATE_ORDER)

    @allure.step('Создать заказ')
    def create_order(self):
        self.main_page_loading_wait()
        self.drag_sauce_to_constructor()
        self.wait_ingredient_sauce_in_constructor()
        self.drag_bun_to_constructor()
        self.wait_button_create_order()
        self.click_on_button_create_order()

