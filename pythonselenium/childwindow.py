import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# compare expected v/s actual list

driver = webdriver.Firefox()
driver.implicitly_wait(8)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

windowsOpen = driver.window_handles #store all windows in list [0th index , 1st index , 2nd index ]
driver.switch_to.window(windowsOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)
driver.close()
driver.switch_to.window(windowsOpen[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
