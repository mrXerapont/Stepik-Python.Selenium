from selenium import webdriver
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_css_selector('button.btn[type=submit]')
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    btn = browser.find_element_by_css_selector('button.btn[type=submit]')
    btn.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()