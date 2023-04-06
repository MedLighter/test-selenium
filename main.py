from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

driver = webdriver.Edge()

def first_test_case(url_="https://www.litres.ru/pages/login/"):
    """Авторизация на сайте"""
    driver.get(url=url_)
    # time.sleep(5)
    email = driver.find_element(by=By.NAME, value='login')
    email.send_keys(os.getenv('email'))
    password = driver.find_element(by=By.ID, value='open_pwd_main')
    password.send_keys(os.getenv('password'))
    button = driver.find_element(by=By.ID, value='login_btn')
    button.click()
    # time.sleep(3)


def second_test_case():
    """Дабавление нескольких книг в отложенные"""
    driver.get(url="https://www.litres.ru")
    # time.sleep(3)
    input_search = driver.find_element(by=By.CLASS_NAME, value="SearchForm-module__input_1E6az")
    input_search.send_keys('Программирование')
    input_search.send_keys(Keys.ENTER)
    time.sleep(7)
    favorite = driver.find_elements(by=By.CLASS_NAME, value="ArtV2-module__like_button_3XOia")
    # print(favorite)
    for _ in range(3):
        favorite[_].click()
        # time.sleep(1)
    driver.get(url="https://www.litres.ru/pages/new_liked/")

    time.sleep(3)

    # ArtV2-module__like_button_3XOia кнопка избранного

    # https://www.litres.ru/search/?q=


def third_test_case(search="Программирование"):
    """Добавление книг в карзину"""
    url_ = f"https://www.litres.ru/search/?q={search}"
    driver.get(url=url_)
    time.sleep(2)
    all_book = driver.find_elements(by=By.CLASS_NAME, value="ArtInfo-modules__wrapper_mS55u")
    time.sleep(2)
    links = []
    for item in all_book[:3]:
        temp = item.find_element(by=By.TAG_NAME, value="a")
        temp2 = temp.get_attribute('href')
        links.append(temp2)
    
    for item in links:
        driver.get(url=item)
        button = driver.find_element(by=By.CLASS_NAME, value="art-buttons__basket")
        button.click()
        time.sleep(1)
    
    driver.get(url="https://www.litres.ru/pages/new_basket/")
    time.sleep(5)
    

try:
    first_test_case()
    second_test_case()
    third_test_case()

except Exception as ex:
    print(ex)
finally:
    driver.close()
    