import time
from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Cart_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    #Locators
    link_checkout_button = '//a[@class ="cart-block__checkout button"]'

    #Getters
    def get_link_checkout_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_checkout_button)))

    # #Actions

    def click_link_checkout_button(self):
        self.get_link_checkout_button().click()
        print("Click checkout button")

    # Methods

    def product_confirmation(self):
        self.driver_g.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        self.get_current_url()
        self.assert_url('https://www.berito.ru/cart/')
        self.get_screenshot()
        self.click_link_checkout_button()
