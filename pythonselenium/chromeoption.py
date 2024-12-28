import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()
#
# Set implicit wait
driver.implicitly_wait(8)

Chrome_option = webdriver.ChromeOptions()
Chrome_option.add_argument("--start-maximized")
Chrome_option.add_argument("headless")
Chrome_option.add_argument("--ignore-certificate-errors") # mostly we will use chrome option for ignoring certification errors

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)


time.sleep(4)