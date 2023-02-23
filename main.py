# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()
userPW = os.environ.get('PASSWORD')

now = datetime.now()
nextWeek = now + timedelta(weeks=1)
print('이번달 :', now.month)
print('다음달 :', nextWeek.month)
clickDate = nextWeek.strftime("%Y%m%d")
print("선택 날짜 : date-"+clickDate)
center = "시민체육광장"
part = "테니스장"
place = "3코트"
subScriptURL = "https://www.gunpouc.or.kr/fmcs/157"

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.gunpouc.or.kr/fmcs/160")  # 로그인 화면
driver.implicitly_wait(15)  # 페이지 다 뜰 때 까지 기다림

# 로그인
driver.find_element(By.ID, "user_id").send_keys("ehddn453")
driver.find_element(By.ID, "user_password").send_keys(userPW)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div/article/div/div/div/div[1]/form/fieldset/div/p[3]/button").click()
driver.implicitly_wait(5)

# 대관 신청
driver.get(subScriptURL)
driver.implicitly_wait(5)

# 센터 선택
driver.find_element(By.XPATH, '//*[@id="center"]/option[text()="'+center+'"]').click()
driver.implicitly_wait(5)

# 시설 선택
driver.find_element(By.XPATH, '//*[@id="part"]/option[text()="'+part+'"]').click()
driver.implicitly_wait(5)

# 코트 선택
driver.find_element(By.XPATH, '//*[@id="place"]/option[text()="'+place+'"]').click()
driver.implicitly_wait(5)

# 조회
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[1]/form/fieldset/div/div/div/button").click()
driver.implicitly_wait(5)


# 다음주 날짜 선택
if now.month == nextWeek.month:
    driver.find_element(By.ID, "date-" + clickDate).click()
else:
    driver.find_element(By.ID, "next_month").click()
    driver.implicitly_wait(5)
    sleep(1)
    driver.find_element(By.ID, "date-" + clickDate).click()
driver.implicitly_wait(5)

# 시간 선택
driver.find_element(By.ID, "checkbox_time_4").click()
driver.find_element(By.ID, "checkbox_time_5").click()
driver.implicitly_wait(5)

# reCAPCHA 클릭 - iframe으로 이동
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[src^="https://www.google.com/recaptcha/api2/"]')
driver.switch_to.frame(iframe)

# reCAPTCHA 체크박스 클릭
driver.find_element(By.CSS_SELECTOR, '.recaptcha-checkbox-border').click()
driver.implicitly_wait(5)

# 원래 iframe으로 이동
driver.switch_to.default_content()

# 페이지 HTML 소스 가져오기
html = driver.page_source
driver.implicitly_wait(5)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')
sleep(2)

# 대관 신청 버튼 클릭
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[6]/div[2]/button").click()
sleep(1)

# ------- 다음 페이지 ---------

# 대표자 입력
driver.find_element(By.ID, "team_nm").send_keys("도미니언")
# 참가 인원 입력
driver.find_element(By.ID, "users").send_keys("4")
# 이용 목적 입력
driver.find_element(By.ID, "purpose").send_keys("개인이용")
# 동의 클릭
driver.find_element(By.ID, "agree_use1").click()
sleep(1)

# reCAPCHA 클릭 - iframe으로 이동
iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[src^="https://www.google.com/recaptcha/api2/"]')
driver.switch_to.frame(iframe)

# reCAPTCHA 체크박스 클릭
driver.find_element(By.CSS_SELECTOR, '.recaptcha-checkbox-border').click()
driver.implicitly_wait(5)

# 원래 iframe으로 이동
driver.switch_to.default_content()

# 페이지 HTML 소스 가져오기
html = driver.page_source
driver.implicitly_wait(5)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')
sleep(2)

# 신청 완료
driver.find_element(By.ID, "chkrecapt_btn").click()
