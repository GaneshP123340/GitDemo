import time
from itertools import count
from tabnanny import process_tokens

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
#Find the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)  # if any item did wait to disply it will help to wait max of 5second if visible within 2 second also will proceed

#
#
#
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(4)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, ".//div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, ".//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation (Functional Testing )
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(input("Please Enter Your PROMOCODE"))
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# wait = WebDriverWait(driver , 10)#explicit wait ... wait for 10 second to validate promocode
# wait.until(expected_conditions.presence_of_elemet_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
