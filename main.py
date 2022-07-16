from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import os

import time

s = Service("/Users/ezeiruezra/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://tinder.com/app/recs")

email_address = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

log_in = driver.find_element(By.XPATH,
                             value='//*[@id="c-1804602209"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')

# Log in via facebook
log_in.click()
time.sleep(2)
facebook_sign_in = driver.find_element(By.XPATH,
                                       value='//*[@id="c761984011"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')
facebook_sign_in.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(10)

enter_email = driver.find_element(By.CSS_SELECTOR, value="#email")
enter_email.send_keys(f"{email_address}")
time.sleep(2)

enter_password = driver.find_element(By.CSS_SELECTOR, value="#pass")
enter_password.send_keys(f"{password}")
time.sleep(2)

login = driver.find_element(By.CSS_SELECTOR, value="#loginbutton")
login.click()

driver.switch_to.window(base_window)
time.sleep(10)

# Clicks the "allow" button on the location pop-up
location_pop_up = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
location_pop_up.click()
time.sleep(3)

# CLicks "not interested" on the notifications pop-up
notifications_pop_up = driver.find_element(By.XPATH, value='//*[@id="c761984011"]/div/div/div/div/div[3]/button[2]/span')
notifications_pop_up.click()
time.sleep(3)

# Clicks "allow cookies" on the Cookies Pop-up
cookies_pop_up = driver.find_element(By.XPATH, value='//*[@id="c-1804602209"]/div/div[2]/div/div/div[1]/div[1]/button')
cookies_pop_up.click()
time.sleep(3)


# Swipes ten times to find a match
for _ in range(10):
    try:
        time.sleep(10)
        try:
            ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
        except NoSuchElementException:
            time.sleep(10)
            ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
    except ElementClickInterceptedException:
        back_to_tinder = driver.find_element(By.XPATH, value='//*[@id="c761984011"]/div/div/div/div/div[3]/button/svg')
        back_to_tinder.click()




