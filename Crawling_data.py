from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException

# WebDriver 설정
driver = webdriver.Chrome()
url = 'https://www.jobkorea.co.kr/starter/passassay/'

# 웹 페이지 접속
driver.get(url)
driver.implicitly_wait(time_to_wait=10)      # 암묵적 대기(Implicit Waits) 10초

# 팝업창 닫기 (selenium으로 접속시 팝업창이 뜬다)
popup_close_btn = driver.find_element_by_xpath('/html/body/div[5]/div/button')
popup_close_btn.click()

# 자기소개서 데이터 모으기
companies_name_list = []       # 회사명을 담을 리스트
data = []       # 자기소개서 질문과 답을 담을 리스트


for n in range (3):     # 이론상 총 1600개의 데이터
    for num_page in range (2, 11):      # 전체 페이지 이동 (10페이지)
        for num_list in range (1, 21):      # 자기소개서 페이지 이동 (1페이지당 20개의 자소서)
            interview_list = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/ul/li[{}]/div[1]/p/a/span'.format(num_list))
            companies_name_list.append(interview_list.text)
            interview_list.click()

            try:
                for i in range (1, 3):      # 자기소개서 내용 수집 (로그인 안할 시 2개의 항목만 미리보기)
                    q_element = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/dl/dt[{}]/button/span[2]'.format(i))      # 질문
                    a_element = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/dl/dd[{}]/div'.format(i))       # 답변

                    question = q_element.text
                    answer = a_element.text
                    data.append([question, answer])     # data 리스트: [[q, a], [q, a], ...]

            except NoSuchElementException:      # 자기소개서중 항목이 1개만 있는 경우
                pass
            except UnexpectedAlertPresentException:     # 등록된 자기소개서가 없어진 경우
                pass
            driver.back()       # 뒤로가기

        if n == 0 and num_page == 10:      # 마지막 페이지라면 10페이지 넘기기 클릭 (처음엔 뒤로 10페이지가 없음)
            skip_10page = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div[2]/p/a').click()
        elif n != 0 and num_page == 10:
            skip_10page = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div[2]/p[2]/a').click()
        else:
            page_list = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[5]/div[2]/ul/li[{}]/a'.format(num_page)).click()

# 웹 드라이버 종료
driver.quit()

# 회사명 데이터를 텍스트 파일로
file_name = './companies_name.txt'
companies_name_list = set(companies_name_list)      # 중복된 회사명 제거

with open(file_name, 'w+', encoding='utf-8') as file:
    file.write('\n'.join(companies_name_list))

# 자기소개서 데이터를 csv 파일로
import pandas as pd
from sklearn.utils import shuffle

interview_data = pd.DataFrame(data, columns=['Q', 'A'])     # 크롤링한 데이터를 데이터프레임으로 변환
interview_data = shuffle(interview_data)       # 데이터프레임을 랜덤하게 섞음

interview_data.to_csv('Interview_Data.csv', index=False, encoding='utf-8')