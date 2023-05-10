from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import loginPage, nameChoosePage, bankManagerActionsPage


sys.stdout = open("../Logger.txt", "w")

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# ---- STEP ONE -----
loginButton = loginPage.LoginPage().getBankManagerLoginButton(driver)
loginButton.click()
# ---- STEP TWO -----
openAccountButton = bankManagerActionsPage.BankManagerActionsPage().getOpenAccountButton(driver)
openAccountButton.click()
# ---- STEP THREE -----
customerDropDown = bankManagerActionsPage.BankManagerActionsPage().getCustomerDropDownMenu(driver)
customerDropDown.select_by_visible_text("Ron Weasly")
currencyDropDown = bankManagerActionsPage.BankManagerActionsPage().getCurrencyDropDownMenu(driver)
currencyDropDown.select_by_visible_text("Pound")
sleep(2)
# ---- STEP FOUR -----
processOrderButton = bankManagerActionsPage.BankManagerActionsPage().getProcessOrderButton(driver)
processOrderButton.click()
sleep(1)
alert = driver.switch_to.alert
alert.accept()

sleep(5)

driver.close()