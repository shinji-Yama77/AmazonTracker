from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ask = input("What do you want to search for on Amazon? ")


PATH = '/Users/shinjiy/Desktop/chromedriver'

driver = webdriver.Chrome(PATH)


driver.get("https://www.amazon.com/")



search = driver.find_element_by_id("twotabsearchtextbox")



search.send_keys(ask)
search.send_keys(Keys.RETURN)



time.sleep(5)

driver.quit()
