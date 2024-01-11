from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "https://www.youtube.com/@CarryMinati/videos"
driver.get(url)
driver.maximize_window()

# driver.find_element(By.XPATH,"//*[@id='tabsContent']/tp-yt-paper-tab[2]/div/div[1]")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#chips > yt-chip-cloud-chip-renderer:nth-child(2)").click()

driver.find_element(By.XPATH,'//*[@id="contents"]')

# //*[@id="contents"]/ytd-rich-item-renderer[1]
