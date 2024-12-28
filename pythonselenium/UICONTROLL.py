import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Find the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
checkboxes = driver.find_elements(By.XPATH, "input[@name='checkBoxOption2']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


# radioButtons = driver.find_elements(By.XPATH, "input[@type='radio']")
#
# print(len(radioButtons))
#
# for radioButton in radioButtons:
#     if radioButton.get_attribute("value") == "radio2":
#         radioButton.click()
#         assert radioButton.is_selected()
#         break
#


time.sleep(8)