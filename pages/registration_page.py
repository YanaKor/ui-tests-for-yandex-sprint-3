import allure
from base.base_object import BaseObject
from base.locators import RegistrationLocators as Registr
from base.locators import LogInFormLocators as LogForm
from support.assertions import Assertions


class RegistrationPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Click on sign in button')
    def click_on_sign_in_btn(self):
        self.click(Registr.SIGN_IN_BUTTON)

    @allure.step('Click on registration link')
    def click_on_register_link(self):
        self.click(Registr.REGISTER_LINK)

    @allure.step('Fill name field')
    def enter_name(self, name):
        self.fill_field(Registr.NAME_FIELD, name)

    @allure.step('Fill email field')
    def enter_email(self, email):
        self.fill_field(Registr.EMAIL_FIELD, email)

    @allure.step('Fill password')
    def enter_password(self, password):
        self.fill_field(Registr.PASSWORD_FIELD, password)

    @allure.step('Click on registration button')
    def click_on_register_btn(self):
        self.click(Registr.REGISTER_BUTTON)

    @allure.step('Checking successful registration')
    def check_title(self):
        self.assert_equal(self.get_text(LogForm.LOGIN_BUTTON), 'Войти')

    @allure.step('Checking for incorrect password error during registration ')
    def check_error_message(self):
        self.assert_equal(self.get_text(Registr.ERROR_MESSAGE), 'Некорректный пароль')
