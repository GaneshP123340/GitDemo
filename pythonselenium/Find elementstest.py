import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


#Find the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


driver.find_element(By.ID, "autosuggest").send_keys("ind")





# countries = driver.find_element(By.CSS_SELECTOR, "li[class='ui-menu-item']")
# print(len(countries))

# Find all elements with the specified CSS selector
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")

# Print the number of matching elements
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text)

# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

# Assert that the value of the element is "India"
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"




time.sleep(8)

