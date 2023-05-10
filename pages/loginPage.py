from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self):
        pass

    def getCustomerLoginButton(self, driver):
        loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button')
        return loginButton

    def getBankManagerLoginButton(self, driver):
        loginButton = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button')
        return loginButton