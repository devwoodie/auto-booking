# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.gunpouc.or.kr/fmcs/160")  # 로그인 화면
driver.implicitly_wait(15)  # 페이지 다 뜰 때 까지 기다림

driver.find_element(By.ID, "user_id").send_keys("ehddn453")
driver.find_element(By.ID, "user_password").send_keys("!b12464530045")
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/section/div/article/div/div/div/div[1]/form/fieldset/div/p[3]/button").click()
driver.implicitly_wait(5)

# 대관 신청
driver.get("https://www.gunpouc.or.kr/fmcs/157")
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[1]/form/fieldset/div/div/ul/li[1]/div/select/option[2]").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[1]/form/fieldset/div/div/ul/li[2]/div/select/option[5]").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[1]/form/fieldset/div/div/ul/li[3]/div/select/option[1]").click()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[1]/form/fieldset/div/div/div/button").click()
driver.implicitly_wait(5)

nowDate = datetime.today()
print(nowDate)
