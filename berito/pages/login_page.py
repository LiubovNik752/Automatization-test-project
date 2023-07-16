import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):
    url = 'https://www.berito.ru/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    auth_button = '//button[@class ="button button_micro button_inverted"]'
    user_name = '//input[@id="sign-in_1"]'
    password = '//input[@id="sign-in_2"]'
    login_button = '//*[@id="auth"]/div/div[1]/div/div[2]/form/div[4]/button'
    main_word = '//div[@class="header-profile__title"]'

    # Getters
    def get_auth_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.auth_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions
    def click_auth_button(self):
        self.get_auth_button().click()
        print("Click auth button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user_name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def authorization(self):
        self.driver_g.get(self.url)
        self.driver_g.maximize_window()
        self.get_current_url()
        self.click_auth_button()
        time.sleep(2)
        self.input_user_name("angel1angelangel@yandex.ru")
        self.input_password("123456")
        time.sleep(2)
        self.click_login_button()
        time.sleep(2)
        self.assert_word(self.get_main_word(), 'Ангелина')
