import allure

from helpers import generate_personal_data
from locators.auth_locators import AuthPageLocators
from pages.base_page import BasePage


class AuthPage(BasePage):
    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_until_not_visible(AuthPageLocators.OVERLAY)

    @allure.step("Клик по кнопке Войти в аккаунт")
    def click_on_button_login_account_on_main_page(self):
        self.click_on_element(AuthPageLocators.BTN_LOGIN_ACCOUNT)

    @allure.step('Ожидание появления заголовка Вход')
    def wait_visibility_header_entrance(self):
        self.wait_for_element(AuthPageLocators.HEADER_ENTRANCE)

    @allure.step("Клик по ссылке Зарегистрироваться")
    def click_on_button_register_new_account(self):
        self.click_on_element(AuthPageLocators.LINK_REGISTER)

    @allure.step('Ожидание появления заголовка Регистрация')
    def wait_visibility_header_register(self):
        self.wait_for_element(AuthPageLocators.HEADER_REGISTER)

    @allure.step("Заполнить форму регистрации личными данными")
    def fill_form_data_register(self, generate_personal_data):
        name, email, password = generate_personal_data
        self.send_keys_to_input(AuthPageLocators.INPUT_NAME, name)
        self.send_keys_to_input(AuthPageLocators.INPUT_EMAIL, email)
        self.send_keys_to_input(AuthPageLocators.INPUT_PASSWORD, password)

    @allure.step("Подтвердить ввод данных кнопкой Зарегистрироваться")
    def click_submit_register(self):
        self.click_on_element(AuthPageLocators.BTN_REGISTER)

    @allure.step('Ожидание появления заголовка Вход')
    def wait_visibility_header_entrance(self):
        self.wait_for_element(AuthPageLocators.HEADER_ENTRANCE)

    @allure.step("Заполнить форму авторизации личными данными")
    def fill_form_data_auth(self, email, password):
        self.send_keys_to_input(AuthPageLocators.INPUT_EMAIL, email)
        self.send_keys_to_input(AuthPageLocators.INPUT_PASSWORD, password)

    @allure.step("Подождать кликабельности кнопки Войти")
    def wait_for_clickable_button_login_account(self):
        self.wait_for_clickable_element(AuthPageLocators.BTN_ENTER)

    @allure.step("Клик по кнопке Войти")
    def click_on_button_login_account(self):
        self.click_on_element(AuthPageLocators.BTN_ENTER)

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_until_not_visible(AuthPageLocators.OVERLAY)

    @allure.step("Скролл до элемента")
    def scroll_to_element_login_account(self):
        element = self.wait_for_element(AuthPageLocators.BTN_PERSONAL_ACCOUNT)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Клик по кнопке Личный кабинет")
    def click_on_button_personal_account(self):
        self.click_on_element(AuthPageLocators.BTN_PERSONAL_ACCOUNT)

    @allure.step("Создание и авторизация уникального пользователя")
    def create_user_and_auth(self, personal_data):
        self.main_page_loading_wait() # ждем загрузки главной страницы
        self.click_on_button_login_account_on_main_page() # нажимаем Войти в аккаунт
        self.click_on_button_register_new_account() # переходим к регистрации пользователя
        self.wait_visibility_header_register() # ждем заголовка Регистрация
        self.fill_form_data_register(personal_data) # заполняем форму регистрации
        self.click_submit_register() # надимаем кнопку Зарегистрироваться
        self.wait_visibility_header_entrance() # ждем появления заголовка Вход
        email = personal_data[1]
        password = personal_data[2]
        self.fill_form_data_auth(email, password) # заполняем форму входа
        self.click_on_button_login_account() # нажимаем кнопку Войти
        self.wait_url_auth() # ждем появления в url /account/profile

    @allure.step('Авторизация созданного пользователя')
    def auth(self, email, password):
        self.main_page_loading_wait()  # ждем загрузки главной страницы
        self.click_on_button_login_account_on_main_page() # нажимаем Войти в аккаунт
        self.wait_visibility_header_entrance() # ждем появления заголовка Вход
        self.fill_form_data_auth(email, password) # заполняем форму входа
        self.wait_for_clickable_button_login_account() # ждем кликабельности кнопки Войти
        self.click_on_button_login_account() # нажимаем кнопку Войти
