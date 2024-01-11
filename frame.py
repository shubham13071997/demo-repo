from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Webdriver
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

time.sleep(4)


driver.execute_script(f"window.scrollBy(0, 300 );")

time.sleep(5)

driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
time.sleep(3)

Outframe=driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(Outframe)



Inframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(Inframe)

time.sleep(3)
# driver.switch_to.default_content()

# driver.switch_to.frame("frame2")
# time.sleep(2)

driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("welcome")

time.sleep(4)
