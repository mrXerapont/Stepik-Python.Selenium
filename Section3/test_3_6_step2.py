import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLessonPages():
    error_text = ""

    @pytest.mark.parametrize('number', ["236895", "236896", "236897"])#, "236898", "236899", "236903", "236904", "236905"])
    def test_page(self, browser, number):
        link = f"https://stepik.org/lesson/{number}/step/1"
        browser.implicitly_wait(5)
        browser.get(link)
        field = browser.find_element_by_tag_name("textarea")
        field.send_keys(str(math.log(int(time.time()))))
        btn = browser.find_element_by_css_selector("button.submit-submission")
        btn.click()
        time.sleep(2)



       # assert True
