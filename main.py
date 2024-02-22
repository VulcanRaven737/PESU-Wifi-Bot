from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time

global username
global password

def random_delay():
    delay = random.uniform(1, 3)  # Random delay between 1 and 3 seconds
    time.sleep(delay)


with open(r"login-id.txt", 'r') as usernameid:    
    id=usernameid.readlines()
    randomness=random.randint(0,len(id))
    for i in range(randomness):
        username=id[i]

with open(r"password.txt", 'r') as password:    
    passw=password.readlines()
    for i in range(len(passw)):
        password=passw[i]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
#initialising the web driver
driver = webdriver.Chrome(options=chrome_options)

# URL of the login page
driver.get('https://192.168.254.1:8090/httpclient.html')
random_delay()

actions = ActionChains(driver)
actions.send_keys(Keys.CONTROL + Keys.F5)
# Find the username and password fields and fill them in
randomclick = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='signin-caption']")))
randomclick.click()
username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
#username_field.click()
#password_field.click()
# Submit the form
actions.send_keys_to_element(username_field, username)
random_delay()
actions.send_keys_to_element(password_field, password)
actions.send_keys(Keys.ENTER)
actions.perform()

# Wait for a few seconds to allow the page to load
time.sleep(3)

# Closes the browser window
driver.quit()
usernameid.close()
password.close()
