from selenium.webdriver.common.by import By
from views.base_view import BaseView


class AddRemoveElementView(BaseView):
    ADD_ELEMENT_ITEM = (By.XPATH, "//button[text()='Add Element']")
    ADDED_ELEMENT_ITEM = (By.XPATH, "//div[@id='elements']/button")

    def __init__(self, driver):
        super().__init__(driver)

    def add_element(self):
        self.wait_for(self.ADD_ELEMENT_ITEM).click()

    def count_elements(self):
        return len(self.find_multiple(self.ADDED_ELEMENT_ITEM))

    def remove_element(self,number):
        self.find_multiple(self.ADDED_ELEMENT_ITEM)[number].click()


# Create a specialized class if there are any differences between browsers
class AddRemoveElementViewFirefox(AddRemoveElementView):
    def __init__(self, driver):
        super().__init__(driver)


class AddRemoveElementViewChrome(AddRemoveElementView):
    def __init__(self, driver):
        super().__init__(driver)


AddRemoveElementView._FIREFOX = AddRemoveElementViewFirefox
AddRemoveElementView._CHROME = AddRemoveElementViewChrome
