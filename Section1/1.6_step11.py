# Вкладываю в качестве решения два файла 1.6_step10 и 1.6_step11
# Основной код идентичен, разница только в ссылке
# 1.6_step10 по умолчанию включена первая регистрационная форма (тест завершается без ошибок), вторая ссылка закоментирована
# 1.6_step11 по умолчанию включена вторая регистрационная форма (тест падает на поле фамилия), первая ссылка закоментирована
# Это сделано на случай если Вам удобно запускать по отдельности
# Или можете просто для запуска нужного теста закоментить/раскоментить нужную строчку

from selenium import webdriver
import time

try:
    # Ссылка на первую форму
    #link = "http://suninjuly.github.io/registration1.html"
    # Ссылка на вторую форму
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input_fname = browser.find_element_by_css_selector("div.first_block input.first")
    input_fname.send_keys("Ivan")
    input_lname = browser.find_element_by_css_selector("div.first_block input.second")
    input_lname.send_keys("Ivanov")
    input_email = browser.find_element_by_css_selector("div.first_block input.third")
    input_email.send_keys("Ivanov@ivan.py")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
