from time import sleep
import sys
from selenium import webdriver
from pages import LoginPage, CustomerActionsPage, NameChoosePage
import os

sys.stdout = open("../Logger.txt", "w")
script_path = os.path.abspath(__file__)
filename = os.path.basename(script_path)

try:
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

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
    transactionsButton = CustomerActionsPage.CustomerActionsPage().getPushButton(driver, '/html/body/div/div/div[2]/div/div[3]/button[1]')
    transactionsButton.click()
    sleep(1)

    driver.close()
    print(f"[{filename}] - SUCCESS - This test script launches a Chrome web driver, navigates to a banking project login page, performs steps to log in as a customer (Harry Potter) and clicks on the transactions button.")
except Exception:
    print(f"[{filename}] - FAILED")
