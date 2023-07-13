from base.base_object import BaseObject
from base.locators import RegistrationLocators as Registr
from base.locators import PersonalAccountLocators as PA
from support.assertions import Assertions


class RegistrationPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_sign_in_btn(self):
        self.click(Registr.SIGN_IN_BUTTON)

    def click_on_register_link(self):
        self.click(Registr.REGISTER_LINK)

    def enter_name(self, name):
        self.type(Registr.NAME_FIELD, name)

    def enter_email(self, email):
        self.type(Registr.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.type(Registr.PASSWORD_FIELD, password)

    def click_on_register_btn(self):
        self.click(Registr.REGISTER_BUTTON)

    def check_url_after_registration(self):
        self.is_present(PA.HEADER_OF_THE_FORM)
        self.assert_equal(self.get_url(), 'https://stellarburgers.nomoreparties.site/login')

    def check_error_message(self):
        self.assert_equal(self.get_text(Registr.ERROR_MESSAGE), 'Некорректный пароль')