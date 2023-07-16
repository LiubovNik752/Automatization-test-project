import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Locators
    link_section_for_men = '//a[@class ="catalog-menu__link" and text() ="Мужчинам"]'
    link_accessory = '//a[@class ="page-menu__link" and text() ="Мужские аксессуары"]'
    link_tie = '//a[@class ="page-menu__link" and text() ="Галстуки"]'
    link_filter_by_price = '//div[@class="filter-popup__toggle" and text() ="Цена"]'
    link_input_price = '//input[@id ="catalog-filter_price_to"]'
    link_apply_button = '//button[@class="filter-popup__apply button"]'
    link_drop_down_list = '//div[@class ="choices__item choices__item--selectable"]'
    link_sorted_by_price = '//div[@id ="choices--filter_sort-item-choice-3"]'
    link_select_first_tie = '//div[@data-id ="5900160"]'
    link_button_add_to_cart = '//div[@class ="product__action-wrapper"]'
    link_cart_icon = '//span[@class ="header-action__info"]'
    link_entry_to_cart = '//a[@class ="cart-popup__to-cart button"]'

    # Getters
    def get_link_section_for_men(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_section_for_men)))

    def get_link_accessory(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_accessory)))

    def get_link_tie(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_tie)))

    def get_link_filter_by_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_filter_by_price)))

    def get_link_input_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_input_price)))

    def get_link_apply_button(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_apply_button)))

    def get_link_drop_down_list(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_drop_down_list)))

    def get_link_sorted_by_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_sorted_by_price)))

    def get_link_select_first_tie(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_select_first_tie)))

    def get_link_button_add_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.presence_of_element_located((By.XPATH, self.link_button_add_to_cart)))

    def get_link_cart_icon(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_cart_icon)))

    def get_link_entry_to_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_entry_to_cart)))

    # Actions

    def click_link_section_for_men(self):
        self.get_link_section_for_men().click()
        print("Click link section for men")

    def click_link_accessory(self):
        self.get_link_accessory().click()
        print("Click link accessory")

    def click_link_tie(self):
        self.get_link_tie().click()
        print("Click link tie")

    def click_link_filter_by_price(self):
        self.get_link_filter_by_price().click()
        print("Click link filter by price")

    def input_price(self, link_input_price):
        self.get_link_input_price().send_keys(link_input_price)
        print("Input price")

    def click_link_apply_button(self):
        self.get_link_apply_button().click()
        print("Click link apply button")

    def click_link_drop_down_list(self):
        self.get_link_drop_down_list().click()
        print("Click link drop down list")

    def click_link_sorted_by_price(self):
        self.get_link_sorted_by_price().click()
        print("Click link sorted by price")

    def click_ink_select_first_tie(self):
        self.get_link_select_first_tie().click()
        print("Click link select first tie")

    def click_link_button_add_to_cart(self):
        self.get_link_button_add_to_cart().click()
        print("Click button add to cart")

    def click_link_cart_icon(self):
        self.get_link_cart_icon().click()
        print("Click entry cart button")

    def click_link_entry_to_cart(self):
        self.get_link_entry_to_cart().click()
        print("Click entry button to cart")

    # Methods

    def find_product(self):
        self.click_link_section_for_men()
        time.sleep(2)
        self.click_link_accessory()
        time.sleep(2)
        self.click_link_tie()
        time.sleep(2)
        self.click_link_filter_by_price()
        time.sleep(2)
        self.input_price(5000)
        time.sleep(2)
        self.click_link_apply_button()
        time.sleep(2)
        self.click_link_drop_down_list()
        time.sleep(2)
        self.click_link_sorted_by_price()
        time.sleep(2)
        self.driver_g.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        self.click_ink_select_first_tie()
        time.sleep(2)
        self.click_link_button_add_to_cart()
        time.sleep(2)
        self.click_link_cart_icon()
        time.sleep(2)
        self.click_link_entry_to_cart()
        time.sleep(2)
