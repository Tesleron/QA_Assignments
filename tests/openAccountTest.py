from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import loginPage, nameChoosePage


sys.stdout = open("../Logger.txt", "w")

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# ---- STEP ONE -----
loginButton = loginPage.LoginPage().getBankManagerLoginButton(driver)
loginButton.click()
sleep(3)
# ---- STEP TWO -----

driver.close()