# 코드 정리하기---------------------------
import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get() #url을 함수 위에다가 변수로 만들어 선언하기
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


# 마지막 페이지가 뭔지 구하는 함수
def extract_indeed_jobs(last_page):
    for page in range(last_page):
        print(f"&start={page*LIMIT}")

# 코드 정리 끝-----------------------------

# /////////////////////////////////////////////////////////////////
# [수정1단계] 두 번째 함수에다가 페이지 요청하는 내용 추가하기.

import requests
from bs4 import BeautifulSoup

LIMIT = 50
# INDEED_URL --> URL 변수명 변경
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL) #매개변수로 URL 넣어주기
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        # 요청할 때를 위해 URL 추가하기.
        result = requests.get(f"{URL}&start={page*LIMIT}")  
        # print(result.status_code) --> result.status_code 동작 실행하게 해줌.

# /////////////////////////////////////////////////////////////////
# [수정 2단계] 두 번째 함수 
def extract_indeed_pages():
    result = requests.get(URL) 
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    # 각 페이지에 있는 일자리를 담을 배열 만들기
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)
    # 일자리를 반환한다.
    return jobs 