from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class NameChoosePage:
    def __init__(self):
        pass

    def getDropDownMenu(self, driver):
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select'))
        return dropdown

    def getSpecificName(self, driver):
        harryPotterName = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select/option[3]')
        return harryPotterName

    def getLoginButton(self, driver):
        loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button')
        return loginButton

