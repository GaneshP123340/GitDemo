import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By

#Find the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

# Linktext >>> <a Stands for Link And Forgot password is linktext ..

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") ## "//parentclass/childclass[no.ofchild]/childofchildclass"
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234") #1st approach
# driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Hello@1234") #2nd  approach
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
# driver.find_element(By.XPATH, "//button[@type='submit']").click() #1st  approach
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()  #2nd  approach



time.sleep(8)