from selenium import webdriver
from selenium.webdriver.common.alert import alert
import time

checkday = input("날짜를 입력하세요")
print(checkday)

temp = input("시간을 입력하세요")
checktime = int(temp) +1
print(checktime)

driver = webdriver.Chrome("D:\Desktop\chromedriver")
driver.implicitly_wait(3)

#예약, 매진체크
check = len(driver.find_elements_by_css_selector(".btn_inq > a > img"))
