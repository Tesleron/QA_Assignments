from selenium.webdriver.common.by import By

class NameChoosePage:
    def __init__(self):
        pass

    def getDropDownMenu(self, driver):
        dropdown = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select')
        return dropdown

    def getSpecificName(self, driver):
        harryPotterName = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div/select/option[3]')
        return harryPotterName

    def getBodyDiv(self, driver):
        body = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div')
        return body

