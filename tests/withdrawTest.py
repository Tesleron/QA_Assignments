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
        sleep(1)
        loginButton = LoginPage.LoginPage().getCustomerLoginButton(driver)
        loginButton.click()
        sleep(1)
        # ---- STEP TWO -----
        nameDropDown = NameChoosePage.NameChoosePage().getDropDownMenu(driver)
        nameDropDown.select_by_visible_text("Harry Potter")
        sleep(1)
        # ---- STEP THREE -----
        loginButton = NameChoosePage.NameChoosePage().getLoginButton(driver)
        loginButton.click()
        sleep(1)

    # ---- STEP ONE -----
    customerLogin()
    # ---- STEP TWO -----
    withdrawButton = CustomerActionsPage.CustomerActionsPage().getPushButton(driver, '/html/body/div/div/div[2]/div/div[3]/button[3]')
    withdrawButton.click()
    sleep(1)
    # ---- STEP THREE -----
    depositText = CustomerActionsPage.CustomerActionsPage().getTextBox(driver, '/html/body/div/div/div[2]/div/div[4]/div/form/div/input')
    depositText.send_keys("22")
    sleep(1)
    withdrawButton = CustomerActionsPage.CustomerActionsPage().getPushButton(driver, '/html/body/div/div/div[2]/div/div[4]/div/form/button')
    withdrawButton.click()
    sleep(2)

    driver.close()
    print(f"[{filename}] - SUCCESS - This test script launches a Chrome web driver, navigates to a banking project login page, performs steps to log in as a customer (Harry Potter), clicks on the withdraw button, and performs a withdrawal operation, which will fail because of sufficient funds in the user.")
except Exception:
    print(f"[{filename}] - FAILED")
