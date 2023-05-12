from time import sleep
import sys
from selenium import webdriver
from pages import LoginPage, CustomerActionsPage, NameChoosePage


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
    sleep(1)
    # ---- STEP THREE -----
    loginButton = NameChoosePage.NameChoosePage().getLoginButton(driver)
    loginButton.click()
    sleep(3)

# ---- STEP ONE -----
customerLogin()
# ---- STEP TWO -----
homeButton = CustomerActionsPage.CustomerActionsPage().getPushButton(driver, '/html/body/div/div/div[1]/button[1]')
homeButton.click()
sleep(1)