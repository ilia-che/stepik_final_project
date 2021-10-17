import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru,en,...(etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_locale = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_locale})
    print("\nstart browser for test..")
    # не забываем указать путь к chromedriver (при необходимости)
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
