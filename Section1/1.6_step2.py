from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options = Options()
chrome_options.add_extension("proxy.zip")

browser  = webdriver.Chrome(chrome_options=chrome_options)

#check 1
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element_by_id("submit_button")


#check2
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")