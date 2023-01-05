from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time, os


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



# load env file.
load_dotenv()

# get variables from env file.
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")

time.sleep(5)
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "input[name='username']"))
)

time.sleep(5)
password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "input[name='password']"))
)


print(username)

time.sleep(5)
username.clear()
username.send_keys(USERNAME)

time.sleep(5)
password.clear()
password.send_keys(PASSWORD)


time.sleep(5)
login = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "button[type='submit']"))
).click()


First_Not_Now = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
).click()

# block notifications.
Seccound_Not_Now = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
).click()


# TODO: fix the time for no sleep.
time.sleep(10000000)