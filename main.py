from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")


username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "input[name='username']"))
)

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "input[name='password']"))
)


print(username)
username.clear()
username.send_keys()

password.clear()
password.send_keys()


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