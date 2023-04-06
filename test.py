from selenium import webdriver
from selenium.webdriver.common.by import By

# Получаем в переменную browser указатель на браузер
browser=webdriver.Edge()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://ispi.cdo.vlsu.ru/login/index.php')

# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.NAME, value='username')
username.send_keys('k1179e6jt')

# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.ID, value='password')
password.send_keys('NA498bli')

#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button=browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
#Нажимаем на кнопку входа
button.click()

try:
    # Проверка что пользователь находится на главной странице сайта
    assert 'Учебный сайт кафедры ИСПИ' in browser.title
    # Проверка что на странице присутствует полное имя пользователя
    assert "<Фамилия Имя Отчество Пользователя>" in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')


# Закрываем браузер
browser.close()
