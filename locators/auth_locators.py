from selenium.webdriver.common.by import By

class AuthPageLocators:
    BTN_LOGIN_ACCOUNT = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx")
    BTN_ENTER = (By.XPATH, ".//button[text()='Войти']")
    LINK_REGISTER = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/register"]')
    BTN_REGISTER = (By.XPATH, '//button[contains(@class, "button_button_type_primary__1O7Bx") and text()="Зарегистрироваться"]')
    HEADER_REGISTER = (By.XPATH, '//h2[text()="Регистрация"]')
    INPUT_NAME = (By.XPATH, '//input[@name="name"]')
    INPUT_EMAIL = (By.XPATH, '//div[label[text()="Email"]]/input')
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password" and @name="Пароль"]')
    HEADER_ENTRANCE = (By.XPATH, '//h2[text()="Вход"]')
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    BTN_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')
    HEADER_PROFILE_PERS_ACCOUNT = (By.LINK_TEXT, "Профиль")
