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
loginButton = loginPage.loginPage().getLoginButton(driver)
loginButton.click()
# ---- STEP TWO -----
nameDropDown = nameChoosePage.NameChoosePage().getDropDownMenu(driver)
nameDropDown.select_by_visible_text("Harry Potter")
# ---- STEP THREE -----
loginButton = nameChoosePage.NameChoosePage().getLoginButton(driver)
loginButton.click()
sleep(5)

driver.close()