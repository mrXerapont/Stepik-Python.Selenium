from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_f = browser.find_element_by_id("answer")
    input_f.send_keys(y)

    chkbox = browser.find_element_by_css_selector("div > input[type='checkbox']")
    chkbox.click()

    rad_btn = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rad_btn)
    rad_btn.click()

    btn = browser.find_element_by_css_selector('button.btn[type=submit]')

    btn.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()