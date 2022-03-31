from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture()
def setUp():
    global product, driver
    product = input("Enter any Product to Search: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    yield

    time.sleep(7)
    driver.close()

def test_case_search_Products(setUp):
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(3)
    driver.find_element_by_name("q").send_keys(product)
    time.sleep(5)
    driver.find_element_by_class_name("L0Z3Pu").click()
    time.sleep(10)
