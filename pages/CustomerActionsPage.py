from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CustomerActionsPage:
    def __init__(self):
        pass

    def getTextBox(self, driver, xpath):
        textbox = driver.find_element(By.XPATH, xpath)
        return textbox

    def getPushButton(self, driver, xpath):
        button = driver.find_element(By.XPATH, xpath)
        return button
