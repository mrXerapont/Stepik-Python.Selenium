from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("input[name='firstname']")
    name.send_keys("Ololosh")

    last_name = browser.find_element_by_css_selector("input[name='lastname']")
    last_name.send_keys("Ololoyev")


    email = browser.find_element_by_css_selector("input[name='email']")
    email.send_keys("O@O.oo")



    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    attach = browser.find_element_by_css_selector("#file")
    attach.send_keys(file_path)

    btn = browser.find_element_by_css_selector('button.btn[type=submit]')
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()