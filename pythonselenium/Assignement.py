import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# compare expected v/s actual list

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
ExpectedList = ['Cucumber - 1 Kg' , 'Raspberry - 1/4 Kg' , 'Strawberry - 1/4 Kg']
ActualList = []
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(4)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    ActualList.append(result.find_element(By.XPATH, "h4").text) #actual list which we are getting from website
    result.find_element(By.XPATH, ".//div/button").click() #list

assert ExpectedList == ActualList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, ".//button[text()='PROCEED TO CHECKOUT']").click()

#Sum Validation (Functional Testing )
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalAmount



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(input("Please Enter Your PROMOCODE"))
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Assignment 2 ... Check where discount amout is less then the total amount or not

DiscountAmount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(DiscountAmount)

assert DiscountAmount < totalAmount