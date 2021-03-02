import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    #chrome_options = Options()
    #chrome_options.add_extension("proxy.zip")
    #browser = webdriver.Chrome(chrome_options=chrome_options)
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()