import allure

from pages.constructor import Constructor


class TestConstructor:
    @allure.suite('Transition suite')
    @allure.title('Successful transition')
    @allure.description('Check transition to sauce tab')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_to_sauces_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_sauce_tab()
        constructor.check_transition_to_sauce_tab()

    @allure.suite('Transition suite')
    @allure.title('Successful transition')
    @allure.description('Check transition to bunks tab')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_to_bunks_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_sauce_tab()
        constructor.click_on_bunks_tab()
        constructor.check_transition_to_bunks_tab()

    @allure.suite('Transition suite')
    @allure.title('Successful transition')
    @allure.description('Check transition to stuffing tab')
    @allure.label('owner', 'Yana')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_transition_to_stuffing_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_stuffing_tab()
        constructor.check_transition_to_stuffing_tab()
