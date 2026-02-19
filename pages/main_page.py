from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def open_login_form(self):
        login_tab = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'tab-login'))
        )
        login_tab.click()

    def enter_email(self, email):
        email_input = self.wait.until(
            EC.presence_of_element_located((By.ID, 'auth__input--enterEmailOrLogin'))
        )
        email_input.send_keys(email)

        continue_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='auth__button--continue']"))
        )
        continue_btn.click()

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='auth__input--enterPassword']"))
        )
        password_input.send_keys(password)

    def click_enter_btn(self):
        self.browser.find_element(By.CSS_SELECTOR, '[data-testid="auth__button--enter"]').click()