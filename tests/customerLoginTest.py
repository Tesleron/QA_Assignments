from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import LoginPage, NameChoosePage



sys.stdout = open("../Logger.txt", "w")

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

def customerLogin():
    # ---- STEP ONE -----
    loginButton = LoginPage.LoginPage().getCustomerLoginButton(driver)
    loginButton.click()
    # ---- STEP TWO -----
    nameDropDown = NameChoosePage.NameChoosePage().getDropDownMenu(driver)
    nameDropDown.select_by_visible_text("Harry Potter")
    # ---- STEP THREE -----
    loginButton = NameChoosePage.NameChoosePage().getLoginButton(driver)
    loginButton.click()
    sleep(5)

customerLogin()

driver.close()