from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	first_name = browser.find_element_by_css_selector(".first:required")
	first_name.send_keys("First")
	last_name = browser.find_element_by_css_selector(".second:required")
	last_name.send_keys("Last")
	email = browser.find_element_by_css_selector(".third:required")
	email.send_keys("Email")

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	time.sleep(1)

	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text

	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	time.sleep(10)
	browser.quit()