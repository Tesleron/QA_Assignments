from time import sleep
from pages.customerLoginPage import loginButton
import sys

sys.stdout = open("../Logger.txt", "w")


def customerLoginButtonStepOne():
    loginButton.click()  # Step 1
    print("Finished step 1")
    sleep(5)
