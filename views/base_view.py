from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser_tag = {
    "firefox": "_FIREFOX",
    "chrome": "_CHROME"
}


class BaseView(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_multiple(self, locator):
        return self.driver.find_elements(*locator)

    @classmethod
    def instance(cls, driver):
        used_browser = driver.caps["browserName"]
        classes = {key: getattr(cls, value, cls) for key, value in browser_tag.items()}
        return classes[used_browser](driver)
