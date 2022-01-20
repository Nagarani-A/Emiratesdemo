from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

# open browser
s = Service("C:\\Users\\nagua\\PycharmProjects\\SeleniumExamples\\drivers\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://www.emirates.com/ae/english/")
driver.maximize_window()
driver.implicitly_wait(10)

# Accept cookies
driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
time.sleep(3)

# Departure
driver.find_element(By.NAME, "clear Departure airport").click()
driver.find_element(By.NAME, "Departure airport").send_keys("Dubai (DXB)")
time.sleep(3)

# Airport arrival
driver.find_element(By.NAME, "Arrival airport").send_keys("Budapest (BUD)")
time.sleep(3)

'''#Passengers

dd=driver.find_element(By.ID, "tcm:196-73543")
s=Select(dd)
#s.select_by_index(1)
#or
#s.select_by_value("50")
s.select_by_visible_text("Economy Class")
p1=s.options#it will give all the webelementss and store in variable
print(p1)
#to print the values in the dropdown
for element in p1:
    p2=element.get_attribute("value")
    print(p2)
    time.sleep(5)
'''
# continue
driver.find_element(By.XPATH, "//*[@id='panel0']/div[2]/div/div/div[2]/section/div[4]/div[1]/div[4]/a").click()
time.sleep(3)

# datepicker

driver.find_element(By.XPATH, "//input[contains(@id,'search-flight-date-picker--depart')]").click()
driver.find_element(By.XPATH,"//div[@id='panel0']/div[2]/div/div/div[2]/section/div[4]/div/div[3]/eol-datefield/eol-calendar/div/div/div[2]/table/tbody/tr[4]/td[6]/a").click()


driver.find_element(By.XPATH, "//input[contains(@id,'search-flight-date-picker--return')]").click()
driver.find_element(By.XPATH,"//div[@id='panel0']/div[2]/div/div/div[2]/section/div[4]/div/div[3]/eol-datefield/eol-calendar/div/div/div[3]/table/tbody/tr[2]/td[4]/a").click()


#Search

driver.find_element(By.XPATH,"//*[@id='panel0']/div[2]/div/div/div[2]/section/div[4]/div[2]/div[3]/form/button").click()
time.sleep(3)

'''# Class
s= driver.find_element(By.ID, "search-flight-class")
s.select_by_visible_text("Economy Class")
time.sleep(5)'''

time.sleep(5)
# driver.quit()
