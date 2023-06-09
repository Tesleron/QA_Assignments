from time import sleep
import sys
from selenium import webdriver
from pages import LoginPage, BankManagerActionsPage
import os

sys.stdout = open("../Logger.txt", "w")
script_path = os.path.abspath(__file__)
filename = os.path.basename(script_path)

try:
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    driver.implicitly_wait(20)  # gives an implicit wait for 20 seconds

    # ---- STEP ONE -----
    sleep(2)
    loginButton = LoginPage.LoginPage().getBankManagerLoginButton(driver)
    loginButton.click()
    # ---- STEP TWO -----
    addCustomerButton = BankManagerActionsPage.BankManagerActionsPage().getCustomersButton(driver, '/html/body/div/div/div[2]/div/div[1]/button[3]')
    addCustomerButton.click()
    sleep(2)
    buttons = BankManagerActionsPage.BankManagerActionsPage().getButtons(driver)
    for button in buttons:
        button.click()
    sleep(2)
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

    # ---- STEP FOUR -----
    addCustomerButton = BankManagerActionsPage.BankManagerActionsPage().getCustomersButton(driver, '/html/body/div/div/div[2]/div/div[1]/button[3]')
    addCustomerButton.click()
    sleep(2)
    # ---- STEP FIVE -----
    buttons = BankManagerActionsPage.BankManagerActionsPage().getButtons(driver)
    for button in buttons:
        button.click()
    sleep(2)

    sleep(1)
    driver.close()
    print(f"[{filename}] - SUCCESS - This test script launches a Chrome web driver, navigates to a banking project login page, performs steps to log in as a bank manager, deletes all customers, adds a customer with first name Moshe, last name Levi, and post code 123, and then closes the driver.")
except Exception:
    print(f"[{filename}] - FAILED")
