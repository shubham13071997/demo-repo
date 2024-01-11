from selenium import webdriver

# from datetime import date

# today = date.today().strftime("%d-%m-%Y")

# import time,os,requests



#Options instance

driver = webdriver.Chrome()

driver.get('http://www.easyhr.in/index.php')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('shubham.patil')
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('PVYHN7')
driver.find_element(By.XPATH,'//*[@id="btn"]').click()
driver.find_element(By.XPATH,'//*[@id="menu"]/ul/li[1]/a/span/b').click()
driver.find_element(By.XPATH,'//*[@id="menu"]/ul/li[1]/ul/li[1]/a/span').click()
#driver.find_element(By.XPATH,'//*[@id="emp_time"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[5]/div[5]/a').click()
import time
time.sleep(30)
driver.close()
driver.quit()