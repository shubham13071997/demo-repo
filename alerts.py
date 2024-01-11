from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.maximize_window()

time.sleep(4)


driver.execute_script(f"window.scrollBy(0, 300 );")

time.sleep(5)


alert=driver.find_element(By.XPATH,'//*[@id="promtButton"]').click()

time.sleep(3)


alert = Alert(driver)

alert.send_keys('Welcome')

# alert=driver.switch_to_alert

alert.accept()

time.sleep(4)

