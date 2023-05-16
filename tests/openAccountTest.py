from time import sleep
import sys
from selenium import webdriver
from pages import LoginPage, NameChoosePage, BankManagerActionsPage
import os

sys.stdout = open("../Logger.txt", "w")
script_path = os.path.abspath(__file__)
filename = os.path.basename(script_path)

try:
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

    # ---- STEP ONE -----
    loginButton = LoginPage.LoginPage().getBankManagerLoginButton(driver)
    loginButton.click()
    # ---- STEP TWO -----
    openAccountButton = BankManagerActionsPage.BankManagerActionsPage().getOpenAccountButton(driver)
    openAccountButton.click()
    # ---- STEP THREE -----
    customerDropDown = BankManagerActionsPage.BankManagerActionsPage().getCustomerDropDownMenu(driver)
    customerDropDown.select_by_visible_text("Ron Weasly")
    currencyDropDown = BankManagerActionsPage.BankManagerActionsPage().getCurrencyDropDownMenu(driver)
    currencyDropDown.select_by_visible_text("Pound")
    sleep(2)
    # ---- STEP FOUR -----
    processOrderButton = BankManagerActionsPage.BankManagerActionsPage().getProcessOrderButton(driver)
    processOrderButton.click()
    sleep(1)
    alert = driver.switch_to.alert
    alert.accept()

    sleep(5)

    driver.close()
    print(f"[{filename}] - SUCCESS - This test script launches a Chrome web driver, navigates to a banking project login page, performs steps to open an account for customer Ron Weasly with currency Pound, and then processes the order.")
except Exception:
    print(f"[{filename}] - FAILED")
