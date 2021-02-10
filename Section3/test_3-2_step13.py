import  unittest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        # for proxy
 #       chrome_options = Options()
  #      chrome_options.add_extension("proxy.zip")
   #     browser = webdriver.Chrome(chrome_options=chrome_options)
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

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
        #time.sleep(10)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)
        input_fname = browser.find_element_by_css_selector("div.first_block input.first")
        input_fname.send_keys("Ivan")
        input_lname = browser.find_element_by_css_selector("div.first_block input.second")
        input_lname.send_keys("Ivanov")
        input_email = browser.find_element_by_css_selector("div.first_block input.third")
        input_email.send_keys("Ivanov@ivan.py")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()

