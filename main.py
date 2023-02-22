# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

now = datetime.now()
nextWeek = now + timedelta(weeks=1)
clickDate = nextWeek.strftime("%Y%m%d")
print("date-"+clickDate)
center = "시민체육광장"
part = "테니스장"
place = "3코트"

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.gunpouc.or.kr/fmcs/160")  # 로그인 화면
driver.implicitly_wait(15)  # 페이지 다 뜰 때 까지 기다림

# 로그인
driver.find_element(By.ID, "user_id").send_keys("ehddn453")
driver.find_element(By.ID, "user_password").send_keys("!b12464530045")
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div/article/div/div/div/div[1]/form/fieldset/div/p[3]/button").click()
driver.implicitly_wait(5)

# 대관 신청
driver.get("https://www.gunpouc.or.kr/fmcs/157")
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
driver.find_element(By.ID, "date-20230227").click()
driver.implicitly_wait(5)

# 시간 선택
driver.find_element(By.ID, "checkbox_time_4").click()
driver.find_element(By.ID, "checkbox_time_5").click()
driver.implicitly_wait(5)

# driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
# driver.implicitly_wait(5)

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
driver.implicitly_wait(5)

# 대관 신청 버튼 클릭
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/section/div/article/div[1]/div/div[6]/div[2]/button").click()
driver.implicitly_wait(5)



