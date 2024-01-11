from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

# from datetime import date

# today = date.today().strftime("%d-%m-%Y")

# import time,os,requests



#Options instance

op = Options()

# op.add_argument("--headless")

op.add_experimental_option("excludeSwitches", ["enable-logging"])

# switch tabs for it dont allow to open new tabs if this is.
#send browser option to webdriver object

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)

driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('secret_sauce')
driver.find_element(By.XPATH,'//*[@id="login-button"]').click()
import time
time.sleep(10)
# price = driver.find_elements(By.CSS_SELECTOR,'div[class="inventory_item_price"]')
# for pr in price:
#     p = pr.get_attribute('innerHTML')
#     print(p)
    
    
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="checkout"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="first-name"]').send_keys('Rahul')
driver.find_element(By.XPATH,'//*[@id="last-name"]').send_keys('Patel')
time.sleep(10)
driver.close()
driver.quit()