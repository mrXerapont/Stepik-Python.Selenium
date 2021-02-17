import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

error_text = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_page(browser, number):
    global error_text
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    field = browser.find_element_by_tag_name("textarea")
    field.send_keys(str(math.log(int(time.time()))))
    btn = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
#btn = browser.find_element_by_css_selector("button.submit-submission")
    btn.click()
    #time.sleep(5)
    WebDriverWait(browser, 5).until(
         EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        )
    rez = browser.find_element_by_css_selector(".smart-hints__hint").text

    if rez != "Correct!":
        error_text += rez
        print("\n"+error_text)

    assert rez == "Correct!", f"Ожидаемый результат 'Correct!', фактический результат ${rez}  \nтекущая строка с ошибкой - ${error_text}"



#if __name__ == "__main__":
 #   pytest.main()