from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")

    x = treasure.get_attribute("valuex")
    y = calc(x)

    input_f = browser.find_element_by_id("answer")
    input_f.send_keys(y)

    chkbox = browser.find_element_by_css_selector("div > input[type='checkbox']")
    chkbox.click()

    rad_btn = browser.find_element_by_css_selector("#robotsRule")
    rad_btn.click()

    btn = browser.find_element_by_css_selector('button.btn[type=submit]')
    btn.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()