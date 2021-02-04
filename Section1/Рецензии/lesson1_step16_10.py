from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

def test_func(browser):
        test_list = {'first':'First name*','second':'Last name*','third':'Email*'}
        for value in test_list.keys():
            try:
                css_selector = '.first_block input.'
                print(css_selector+value)
                input = browser.find_element_by_css_selector(css_selector+value)
                input.send_keys("test")
            except NoSuchElementException:
                print("Cannot locate option with value: %s" % test_list[value])
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        time.sleep(10)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
                
try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля  
    test_func(browser)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
