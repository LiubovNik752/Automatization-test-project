
import self as self
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Payment_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    finish_button = '//button[@id ="finish"]'


    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))


    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")


    # Methods
    def payment(self):
        self.get_current_url()
        self.click_finish_button()
        time.sleep(3)




