from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time, os, requests


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



# load env file.
load_dotenv()

# get variables from env file.
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
# KEYWORD = {} -> to add usernames from json file right here\
#                   and append it in keyword dict and make a loop for all usernames


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

time.sleep(7)
First_Not_Now = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
).click()

time.sleep(5)
# block notifications.
Seccound_Not_Now = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))
).click()


time.sleep(5)
searchDIV = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", "svg[aria-label='Search']"))
).click()


time.sleep(3)
searchInput = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "_aauy"))
)

keyword = "nasa"

time.sleep(5)
searchInput.clear()


time.sleep(5)
searchInput.send_keys(keyword)

# to send Enter key and search for it:
time.sleep(5)
Seccound_Not_Now = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, f"//div[contains(text(), '{keyword}')]"))
).click()

# scrolling the user page

time.sleep(3)
driver.execute_script(
    "window.scrollTo(0, 4000);"
)
"""TODO:
we should get scrolling 'y' position from there pages 
"""

# get images
images = driver.find_elements(By.XPATH, "//img")

images = [image.get_attribute('src') for image in images]

# download images
"""
path = os.getcwd()

path = os.path.join(path, keyword)

os.mkdir(path)
"""
# fetching all posts.
posts = []
links = driver.find_elements(By.XPATH, "//a")

for link in links:
    post = link.get_attribute('href')
    
    if '/p/' in post:
        posts.append(post)

print(posts)

#  Download posts
# TODO: counter is for name the images so i should to changes

download_url = ''
counter = 0

for post in posts:
    counter += 1
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    time.sleep(7)

    if driver.find_element("css selector", "img[style='object-fit: cover;']") is not None:
        download_url = driver.find_element("css selector", "img[style='object-fit: cover;']").get_attribute('src')
        r = requests.get(download_url)
        with open(f"{keyword}-{str(counter)}.png", "wb") as h:
            h.write(r.content)
    else:
        download_url = driver.find_element("css selector", "video[type='video/mp4']").get_attribute('src')
        r = requests.get(download_url)
        with open(f"{keyword}-{str(counter)}.mp4", "wb") as h:
            h.write(r.content)


# TODO: fix the time for no sleep.
time.sleep(10000000)