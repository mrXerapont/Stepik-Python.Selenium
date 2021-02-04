from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



link = "http://suninjuly.github.io/huge_form.html"

try:

# for proxy
#     chrome_options = Options()
#     chrome_options.add_extension("proxy.zip")
#     browser = webdriver.Chrome(chrome_options=chrome_options)

#without proxy
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
