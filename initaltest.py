__author__ = 'icog-labs'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#create a new firefox session
emailID = "sophia.v1.api@gmail.com"
passwd= "v12345678"

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

wait = WebDriverWait(driver,10)


driver.get("https://plus.google.com")

account = driver.find_element_by_css_selector('#Email');

