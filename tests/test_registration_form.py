import allure

from test_data import data
from pages.registration_page import RegistrationPage


class TestRegistrationForm:
    @allure.suite('Registration suite')
    @allure.title('Successful registration')
    @allure.description('Checking registration with valid data')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_registration(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.click_on_sign_in_btn()
        registration_page.click_on_register_link()
        registration_page.enter_name(data.new_user_name)
        registration_page.enter_email(data.new_user_email)
        registration_page.enter_password(data.password)
        registration_page.click_on_register_btn()
        registration_page.check_title()

    @allure.suite('Registration suite')
    @allure.title('Unsuccessful registration')
    @allure.description('Checking registration with invalid data')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_unsuccessful_registration(self, driver):
        registration_page = RegistrationPage(driver)
        registration_page.click_on_sign_in_btn()
        registration_page.click_on_register_link()
        registration_page.enter_name(data.name)
        registration_page.enter_email(data.email)
        registration_page.enter_password('1')
        registration_page.click_on_register_btn()
        registration_page.check_error_message()
