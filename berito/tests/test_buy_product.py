from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.login_page import Login_page

def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True) # Не закрывает браузер после выполнения кода
    g = Service('/All/python_selenium/chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)

    print("Start test")

    login = Login_page(driver_g)
    login.authorization()

    mp = Main_page(driver_g)
    mp.find_product()

    cp = Cart_page(driver_g)
    cp.product_confirmation()
