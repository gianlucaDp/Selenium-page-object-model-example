import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
from views.home_view import HomeView


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption('browser').lower()
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=firefox_service(GeckoDriverManager().install()))

    # Add more browsers here if needed
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
