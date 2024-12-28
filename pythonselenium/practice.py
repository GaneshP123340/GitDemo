import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Find the element

driver = webdriver.Chrome()
driver.get("blob:https://web.whatsapp.com/6062be0b-9312-44b2-b7d3-207442de5ecd")


time.sleep(4)