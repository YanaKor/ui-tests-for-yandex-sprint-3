import allure

from pages.logout import LogoutFromAccount
from pages.login_page import LoginPage
from test_data import data


class TestLogout:
    @allure.suite('Sign out suite')
    @allure.title('Successful logout')
    @allure.description('Logout by clicking on logout button in personal account')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_by_clicking_on_logout_button_in_personal_account(self, driver):
        logout = LogoutFromAccount(driver)
        login = LoginPage(driver)

        login.click_on_personal_account_button()
        login.enter_email_on_login_page(data.email)
        login.enter_password_on_login_page(data.password)
        login.click_on_login_btn()
        login.click_on_personal_account_button()
        logout.click_on_logout_button()
        logout.check_text_after_logout()
