import allure

from base.base_object import BaseObject
from support.assertions import Assertions
from base.locators import LogoutLocators as Logout
from base.locators import PersonalAccountLocators as PA


class LogoutFromAccount(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Clicking on logout button')
    def click_on_logout_button(self):
        self.click(Logout.LOGOUT_BUTTON)

    @allure.step('Checking successfully logout')
    def check_text_after_logout(self):
        self.assert_equal(self.get_text(PA.HEADER_OF_THE_FORM), 'Вход')
