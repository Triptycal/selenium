from selenium import webdriver
from selenium.webdriver.common.by imprt By
import time
driver=webdriver.Chrome()

##driver.get('http://www.google.co.uk')

driver.get("file:///C:/Users/Administrator/Documents/Selenium/copy.html")
element1=driver.find_element_by_name("msg1")

element1.send_keys("Mimi is BACK 1234")

time.sleep(3)
Button1=driver.find_element(by=By.NAME, value="btn1")
Button1.click()
time.sleep(3)

Button2=driver.find_element(by=By.ID, value="B")
Button2.click()
time.sleep(3)

Button3=driver.find_element_by_name("btn3")
Button3.click()

element2=driver.find_element(by=By.NAME,value="msg2"

data=element2.get_attribute("value")

print("=================================",data)

element3=driver.find_element(by=By.ID,value="T"

data1=element3.text
print("=================================",data1)

time.sleep(3)
driver.quit()