from selenium import webdriver
from pages.main_page import MainPage

def test_auth(open_browser):
    auth_page = MainPage(open_browser)

    auth_page.open_login_form()
    auth_page.enter_email('daniil.efimow@mail.ru')
    auth_page.enter_password('dandris2003')
    auth_page.click_enter_btn()