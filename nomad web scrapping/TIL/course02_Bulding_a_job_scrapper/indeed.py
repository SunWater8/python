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
    # for page in range(last_page): --> 테스트하기 위해 페이지 수만큼 반복하지 말기
    result = requests.get(f"{URL}&start={0*LIMIT}") # 테스트하기 위해 page를 0으로 수정
    #  div의 class가 job_seen_beacon으로 되어 있는거 모조리 찾아내기.
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class":"job_seen_beacon"})

    print(results)
    # 일자리를 반환한다.
    return jobs 



# 두 번째 함수 수정 - 반복문 사용해서 일자리 리스트 출력하기.
def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page): --> 테스트하기 위해 페이지 수만큼 반복하지 말기
    result = requests.get(f"{URL}&start={0*LIMIT}") # 테스트하기 위해 page를 0으로 수정
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("h2", {"class":"jobTitle"})
    # 반복문 이용해서 배열로 되어 있는 results를 나열하기
    for result in results:
        # 각 구직카드마다 가지고 있는 타이틀 추출하기 - jobTitle라는 class명을 가진 h2 찾기
        # print(result.find("h2", {"class":"jobTitle"})) --> 테스트로 출력해보기
        title = result.find("span", title=True).string
        # anchor에 들어 있는 title을 추출하기 - a태그의 title이 구직카드의 제목이므로
        print(title) #각각의 구직카드 제목이 줄바꿈으로 출력
    print(len(results)) #몇 개의 구직카드 제목이 출력되는지 알아보기
    return jobs 


# /////////////////////////////////////////////////////////////////
# 코드 정리하기
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
    jobs = []
    result = requests.get(f"{URL}&start={0*LIMIT}") 
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("h2", {"class":"jobTitle"})
    for result in results:
        title = result.find("span", title=True).string
        print(title) 
    print(len(results)) 
    return jobs 
# 코드 정리 끝