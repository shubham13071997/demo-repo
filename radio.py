from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://demoqa.com/")
driver.maximize_window()

time.sleep(4)

# scroll_to=driver.find_element(By.XPATH,'(//*[@class="avatar mx-auto white"])[1]').click()
scroll_to=driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]')
time.sleep(3)


actions = ActionChains(driver)
actions.move_to_element(scroll_to)
time.sleep(3)
actions.perform()
time.sleep(8)

# scroll_to.click()
# time.sleep(4)
driver.find_element(By.XPATH,'(//*[@class="avatar mx-auto white"])[1]').click()

time.sleep(5)


# Rb=driver.find_element(By.XPATH,'//*[@id="item-2"]')
# actions.move_to_element(Rb)
# time.sleep(3)
# actions.perform()

driver.execute_script(f"window.scrollBy(0,500 );")

# driver.find_element(By.XPATH,'(//*[@class="avatar mx-auto white"])[1]').click()
driver.find_element(By.XPATH,'//*[@id="item-2"]').click()


time.sleep(7)

driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
# rb=driver.find_element(By.CSS_SELECTOR,'label[class="custom-control-label"][for="yesRadio"]')
time.sleep(4)
print('abc')
# rb.click()
#yesRadio

time.sleep(8)



