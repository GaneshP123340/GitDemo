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

#JavaScript runing with help of python  for scrolling

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")  # will ignore certification errors

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,100);")
driver.execute_script("window.scrollBy(0,500);")
driver.execute_script("window.scrollBy(0,900);")
driver.execute_script("window.scrollBy(0,document.body.scrollTop);")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.execute_script("window.scrollBy(0,document.body.scrollTop);")
time.sleep(5)
driver.get_screenshot_as_file("screen.png")
