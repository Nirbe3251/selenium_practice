import pytest
from selenium import webdriver


@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome()
    browser.get('https://www.litres.ru/')

    yield browser

    browser.quit()