from time import sleep
import sys
from selenium import webdriver
from pages import LoginPage, BankManagerActionsPage

sys.stdout = open("../Logger.txt", "w")
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# ---- STEP ONE -----
loginButton = LoginPage.LoginPage().getBankManagerLoginButton(driver)
loginButton.click()
# ---- STEP TWO -----
addCustomerButton = BankManagerActionsPage.BankManagerActionsPage().getAddCustomerButton(driver, '/html/body/div/div/div[2]/div/div[1]/button[1]')
addCustomerButton.click()
# ---- STEP THREE -----
firstNameText = BankManagerActionsPage.BankManagerActionsPage().getTextBox(driver, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input')
firstNameText.send_keys("Moshe")
lastNameText = BankManagerActionsPage.BankManagerActionsPage().getTextBox(driver, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input')
lastNameText.send_keys("Levi")
postCodeText = BankManagerActionsPage.BankManagerActionsPage().getTextBox(driver, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input')
postCodeText.send_keys("123")
sleep(2)

addCustomerButton = BankManagerActionsPage.BankManagerActionsPage().getAddCustomerButton(driver, '/html/body/div/div/div[2]/div/div[2]/div/div/form/button')
addCustomerButton.click()
sleep(2)

alert = driver.switch_to.alert
alert.accept()

sleep(1)
driver.close()