
import self as self
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Client_information_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    first_name = '//input[@id ="first-name"]'
    last_name = '//input[@id ="last-name"]'
    postal_code = '//input[@id ="postal-code"]'
    continue_button = '//input[@id ="continue"]'


    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")


    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("user")
        self.input_last_name("testovyi")
        self.input_postal_code("1234")
        self.click_continue_button()
        time.sleep(3)



