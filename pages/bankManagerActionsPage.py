from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BankManagerActionsPage:
    def __init__(self):
        pass

    def getOpenAccountButton(self, driver):
        dropdown = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]')
        return dropdown

    def getProcessOrderButton(self, driver):
        dropdown = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
        return dropdown

    def getCustomerDropDownMenu(self, driver):
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select'))
        return dropdown

    def getCurrencyDropDownMenu(self, driver):
        dropdown = Select(driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select'))
        return dropdown

