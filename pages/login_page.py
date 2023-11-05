import allure

from base.base_object import BaseObject
from base.locators import LogInFormLocators as Login, Urls
from support.assertions import Assertions


class LoginPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Clicking on login button on main page')
    def click_on_login_btn_on_main_page(self):
        self.click(Login.LOGIN_BUTTON_ON_MAIN_PAGE)

    @allure.step('Clicking on personal account button')
    def click_on_personal_account_button(self):
        self.click(Login.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Opening the registration form')
    def open_registration_form(self):
        self.go_to_url(Urls.REGISTRATION_FORM_URL)

    @allure.step('Clicking on login button on registration/recovery form')
    def click_on_login_btn_on_register_and_recovery_form(self):
        self.click(Login.LOGIN_BUTTON_FROM_REGISTER_AND_RECOVERY_PAGE)

    @allure.step('Opening recovery form')
    def open_recovery_form(self):
        self.go_to_url(Urls.RECOVERY_FORM_URL)

    @allure.step('Fill email')
    def enter_email_on_login_page(self, email):
        self.fill_field(Login.LOGIN_EMAIL_FIELD, email)

    @allure.step('Fill password')
    def enter_password_on_login_page(self, password):
        self.fill_field(Login.LOGIN_PASSWORD_FIELD, password)

    @allure.step('Clicking on login button')
    def click_on_login_btn(self):
        self.click(Login.LOGIN_BUTTON)

    @allure.step('Checking successfully login')
    def check_text_after_login(self):
        self.assert_equal(self.get_text(Login.HEADER_ON_MAIN_PAGE), 'Соберите бургер')


