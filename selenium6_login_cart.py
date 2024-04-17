from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Edge()
driver.get("http://saucedemo.com")

try:
  user=driver.find_element("id","user-name")
  user.send_keys("standard_user")
  time.sleep(1)
  pswd=driver.find_element("id","password")
  pswd.send_keys("secret_sauce")
  time.sleep(1)
  submit=driver.find_element("id","login-button")
  submit.send_keys(Keys.RETURN)
  time.sleep(2)
  elt=driver.find_element("xpath", "//div[contains(text(),'Sauce Labs Backpack')]/ancestor::div[@class='inventory_item']")
# print(elt.get_attribute('innerHTML'))
  clk=elt.find_element("id","add-to-cart-sauce-labs-backpack")
  print(clk.text)
  clk.send_keys(Keys.RETURN)
except Exception as err:
    print("error:", err)
time.sleep(5)
driver.close()

