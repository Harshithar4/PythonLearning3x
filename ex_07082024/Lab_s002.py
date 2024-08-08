import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://google.com")
driver.maximize_window()
time.sleep(2)