from selenium.webdriver.common.by import By

from views.add_remove_elements_view import AddRemoveElementView
from views.base_view import BaseView


class HomeView(BaseView):
    ADD_RMV_ELEMENT_ITEM = (By.XPATH, r"//a[contains(@href,'/add_remove_elements/')]")

    def __init__(self, driver):
        super().__init__(driver)
        driver.get("http://the-internet.herokuapp.com/")

    def nav_to_add_remove_elements(self):
        self.wait_for(self.ADD_RMV_ELEMENT_ITEM).click()
        return AddRemoveElementView.instance(self.driver)
