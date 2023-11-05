import allure

from pages.personal_account import PersonalAccountPage


class TestPersonalAccount:
    @allure.suite('Personal account suite')
    @allure.title('Successful transition')
    @allure.description('Checking transition to personal account')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_transition_by_clicking_on_personal_account_button(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.check_header_after_clicking_on_personal_account()

    @allure.suite('Personal account suite')
    @allure.title('Successful transition')
    @allure.description('Checking transition to constructor by clicking on logo')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_from_personal_account_to_constructor_by_clicking_on_logo(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.click_on_logo()
        personal_account.check_header_after_transition_from_personal_account()

    @allure.suite('Personal account suite')
    @allure.title('Successful transition')
    @allure.description('Checking transition to constructor by clicking on constructor')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_from_personal_account_to_constructor_by_clicking_on_constructor(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.click_on_constructor()
        personal_account.check_header_after_transition_from_personal_account()
