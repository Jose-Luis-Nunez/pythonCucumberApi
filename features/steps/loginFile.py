from behave import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/prasanth/Downloads/chromedriver_Linux64/chromedriver"
chrome_service = Service(executable_path=chrome_driver_path)


@given('Launching chrome Browser')
def launchBrowser(context):
    context.driver = WebDriver(service=chrome_service)


@when('Open caratlane Login page')
def openLoginURL(context):
    context.driver.maximize_window()
    context.driver.get("https://www.caratlane.com/login")


@when('Enter userName "{email}"')
def enterEmail (context, email):
    context.driver.find_element(by=By.XPATH, value="//*[@name= 'emailMobile']").send_keys(email)


@when('click continue to login butotn')
def clicContinueToLoginCta(context) :
    context.driver.find_element(by=By.XPATH, value="//*[text(='CONTINUE TO LOGIN']").click()


@when('Enter Password "{Pwd}"')
def enterPassword(context, Pwd):
    print('------------------>', Pwd)
    time.sleep(5)
    context.driver.find_element(by=By.XPATH, value="//*[@name= 'password' ]").send_keys(Pwd)
@when('click on the Login Button')
def clickSubmitButton(context):