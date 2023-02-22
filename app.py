import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()

user_email = os.environ['EMAIL']
user_password = os.environ['PASSWORD']

os.environ['PATH'] += r"./drivers/chromedriver.exe"

driver = webdriver.Chrome()
driver.get("https://app.joinsuperset.com/")
driver.implicitly_wait(20)
emailInput = driver.find_element(By.ID,'email').send_keys(user_email)
passwordInput = driver.find_element(By.ID,'password').send_keys(user_password)
loginBtn = driver.find_element(By.CLASS_NAME,'btn-primary').click()


time.sleep(10)
driver.quit()

# sampleDom = driver

# print('jknjk')