import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




driver = webdriver.Firefox()
driver.implicitly_wait(8)

driver.get("https://the-internet.herokuapp.com/iframe")


Caution = driver.find_element(By.XPATH, "//div[@role = 'alert']").text
print(Caution)
driver.find_element(By.XPATH, "//div[@role = 'alert']/button").click()

driver.switch_to.frame("mce_0_ifr")    # mandatory to switch to frame . then only you can find the element otherwise it will throw an error no element find .

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
