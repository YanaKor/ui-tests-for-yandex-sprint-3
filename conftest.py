import pytest
from selenium import webdriver

from base.locators import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)

    yield driver

    driver.quit()
