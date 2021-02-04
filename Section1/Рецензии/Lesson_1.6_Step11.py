from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block input.form-control.first")
    input1.send_keys("Sergey")
    input2 = browser.find_element_by_css_selector(".first_block input.form-control.second")
    input2.send_keys("Vyakhirev")
    input3 = browser.find_element_by_css_selector(".first_block input.form-control.third")
    input3.send_keys("asd@adfs.ru")
    input4 = browser.find_element_by_css_selector(".second_block input.form-control.first")
    input4.send_keys("89161112233")
    input5 = browser.find_element_by_xpath("//div[@class=\"second_block\"]/div/input[@class=\"form-control second\"]")
    input5.send_keys("Moscow")    
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
        
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла