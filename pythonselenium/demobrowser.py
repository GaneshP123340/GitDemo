import time

from selenium import webdriver

#chromedriver service - selenium - 160>160chrome driver
# incase if browser is older and not supporting the library or incase of vpn ( chack the chrome version '120.4354'then download chrome driver manually , set path to codedriver , copy the path and paste in service  )


# service_obj = service("/user/ganesh/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

print('******************************************************************')
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")











time.sleep(4)