from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import Webdriver
driver = webdriver.Chrome()

driver.get("https://biharbhumi.bihar.gov.in/Biharbhumi/Default")
driver.maximize_window()

time.sleep(5)

element=driver.find_element(By.XPATH,'//*[@id="select"]')
drp=Select(element)

drp.select_by_visible_text("रजिस्टर-II अद्यतन लॉगिन")
driver.implicitly_wait(10)
# print('now waiting time')
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])


driver.find_element(By.XPATH,'//*[@id="txt_UserName"]').send_keys('shubham')
driver.find_element(By.XPATH,'//*[@id="txt_Password"]').send_keys('shubh1234')
time.sleep(3)

state=driver.find_element(By.XPATH,'//*[@id="cbo_District_Code"]')
drp=Select(state)
time.sleep(3)
# drp.select_by_visible_text("Aurangabad")
drp.select_by_value("34")

time.sleep(3)

taluka=driver.find_element(By.XPATH,'//*[@id="cbo_Circle_Code1"]')
drp=Select(taluka)
time.sleep(3)
# drp.select_by_visible_text("Aurangabad")
drp.select_by_value("11")

time.sleep(5)

s = driver.find_element(By.XPATH,'//*[@id="login"]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[10]/td[3]')
s=s.text[:-1]
print(s)

res= None
flag_idx = None
for i in range(len(s)):
    
    if s[i] in "+-/*":
        flag_idx = i
if s[flag_idx]=='+':
    res = int(s[0:flag_idx]) + int(s[flag_idx+1:])
print(res)

driver.find_element(By.XPATH,'//*[@id="txtResult"]').send_keys(res)
time.sleep(4)
# driver.find_element(By.XPATH,'<span id="txtNum2">----</span>')

driver.find_element(By.XPATH,'//*[@id="btn_Login"]').click()
time.sleep(3)



# s = "7 + 82"
# res= None
# flag_idx = None
# for i in range(len(s)):
    
#     if s[i] in "+-/*":
#         flag_idx = i
# if s[flag_idx]=='+':
#     res = int(s[0:flag_idx]) + int(s[flag_idx+1:])

# print(int(s[:flag_idx]))
# print(int(s[flag_idx+1:]))
# print(res)
# windowIDs=driver.window_handles()
# time.sleep(5)
# print(len(windowIDs))
# pwindowID = windowIDs[0]
# cwindowID = windowIDs[1]


# driver.quit()
# print('driver closed ')