from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseObject:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def fill_field(self, locator, text):
        self.is_visible(locator).send_keys(text)

    def click(self, locator):
        self.is_clickable(locator).click()

    def get_text(self, locator):
        return self.is_visible(locator).text

    def go_to_url(self, url):
        self.driver.get(url)
