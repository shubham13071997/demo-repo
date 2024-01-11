from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://www.flipkart.com/"
driver.get(url)
driver.find_elements(By.TAG_NAME, 'h2')
time.sleep(10)
driver.quit()
