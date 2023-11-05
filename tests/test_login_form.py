import allure

from test_data import data
from pages.login_page import LoginPage


class TestLoginPage:
    @allure.suite('Authorization suite')
    @allure.title('Successful login')
    @allure.description('Login from main page')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_from_main_page(self, driver):
        login_page = LoginPage(driver)

        login_page.click_on_login_btn_on_main_page()
        login_page.enter_email_on_login_page(data.email)
        login_page.enter_password_on_login_page(data.password)
        login_page.click_on_login_btn()
        login_page.check_text_after_login()

    @allure.suite('Authorization suite')
    @allure.title('Successful login')
    @allure.description('Login from personal account')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_from_personal_account(self, driver):
        login_page = LoginPage(driver)

        login_page.click_on_personal_account_button()
        login_page.enter_email_on_login_page(data.email)
        login_page.enter_password_on_login_page(data.password)
        login_page.click_on_login_btn()
        login_page.check_text_after_login()

    @allure.suite('Authorization suite')
    @allure.title('Successful login')
    @allure.description('Login from registration form')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_from_registration_form(self, driver):
        login_page = LoginPage(driver)

        login_page.open_registration_form()
        login_page.click_on_login_btn_on_register_and_recovery_form()
        login_page.enter_email_on_login_page(data.email)
        login_page.enter_password_on_login_page(data.password)
        login_page.click_on_login_btn()
        login_page.check_text_after_login()

    @allure.suite('Authorization suite')
    @allure.title('Successful login')
    @allure.description('Login from recovery form')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_from_recovery_form(self, driver):
        login_page = LoginPage(driver)

        login_page.open_recovery_form()
        login_page.click_on_login_btn_on_register_and_recovery_form()
        login_page.enter_email_on_login_page(data.email)
        login_page.enter_password_on_login_page(data.password)
        login_page.click_on_login_btn()
        login_page.check_text_after_login()
