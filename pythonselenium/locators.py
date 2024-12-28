import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Find the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#selenium provides locators
# ID , Xpath , CSSSelector , name , LinkText

# driver.find_element(By.N = "email")

# driver.find_element(By.Name,"email").send_keys("ganesh123@")

driver.find_element(By.NAME,'email').send_keys("ganesh123@gmail.com")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("123456789")
driver.find_element(By.ID,'exampleCheck1').click()
driver.find_element(By.NAME,'bday').send_keys("14/4/1999")


# //tagname[@attribute='value'] #to Create Xpath
# tagname[attribute='value'] #to Create CSSSelector #id , Classname

driver.find_element(By.CSS_SELECTOR,"input[name='name']" ).send_keys('Ganesh')
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static drop down
Dropdown= Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
Dropdown.select_by_visible_text("Female")
Dropdown.select_by_index(0)
# Dropdown.select_by_value()  # if it is declare


driver.find_element(By.XPATH,"//input[@type='submit']" ).click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "success" in message # help in validation of text ,  success is present in the message(variable)
# if not match throw assertion error
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()





time.sleep(8)
