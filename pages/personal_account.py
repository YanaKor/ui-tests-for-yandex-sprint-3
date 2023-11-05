import allure

from base.base_object import BaseObject
from support.assertions import Assertions
from base.locators import LogInFormLocators, PersonalAccountLocators as PA


class PersonalAccountPage(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Clicking on personal account button')
    def click_on_personal_account_button(self):
        self.click(LogInFormLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Checking title')
    def check_header_after_clicking_on_personal_account(self):
        self.assert_equal(self.get_text(PA.HEADER_OF_THE_FORM), 'Вход')

    @allure.step('Clicking on logo')
    def click_on_logo(self):
        self.click(PA.LOGO)

    @allure.step('Clicking on constructor')
    def click_on_constructor(self):
        self.click(PA.CONSTRUCTOR)

    @allure.step('Checking header after transition from personal account')
    def check_header_after_transition_from_personal_account(self):
        self.assert_equal(self.get_text(LogInFormLocators.HEADER_ON_MAIN_PAGE), 'Соберите бургер')
