# 이전 수업 배웠던 내용
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    pages.append(int(link.string))
max_page = pages[-1]


print("==============================")
print("2.5 Requesting Each Page ")
# request를 여러개 만들어 수동으로 request 내보내기.
# 최대 페이지 수만큼 request를 보내기

range(max_page) # ranage()함수: 괄호안에 넣은 수 만큼 크기의 배열을 만들어 줌
print(range(max_page)) #range(0, 5) --> 0부터 5까지 내용이 있다는 의미
# 반복문 이용해 배열의 처음부터 끝까지 출력하기.
for n in range(max_page):
    print(n) # 줄바꿈으로 0 1 2 3 4 출력됨.

# range의 현재 값을 indeed에서 가져온 요소 개수만큼 곱해주기
for n in range(max_page):
    print(f"start={n*50}")
# 출력 내용:
"""
start=0
start=50
start=100
start=150
start=2000
"""

# 코드 정리하기.
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    pages.append(int(link.string))
max_page = pages[-1]

for n in range(max_page):
    print(f"start={n*50}")
# 코드 정리 끝


# 반복문 앞의 코드가 길고 반복적으로 쓰일 수 있으므로 함수로 만들어 indeed파일로 따로 이사시키기. 
"""
# 함수로 만들면서 변경된 변수 이름 
indeed_result --> result
indeed_soup --> soup
"""
# 코드 정리 -- 첫 번째 함수만 적용했을 때.
from indeed import extract_indeed_pages

max_indeed_pages = extract_indeed_pages()
print(max_indeed_pages) # 5
# 코드 정리 끝

# 코드 정리하기
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()
extract_indeed_jobs(last_indeed_page)
"""
# 출력 결과 내용
$start=0
$start=50
$start=100
$start=150
$start=200
"""
# 코드 정리 끝

# /////////////////////////////////////////////////////////////////
# 페이지를 요청하기 --> indeed.py가서 두 번째 함수 수정.(수정 1단계 보러 가기.)
# result.status_code 코드 실행 결과
"""
200
200
200
200
200
200
""" 
# status code가 200이 뜨므로 정상적으로 url 요청이 되었음을 알 수 있다.

# /////////////////////////////////////////////////////////////////
# 각 페이지로 가서 일자리 정보를 추출한 후 함수 어딘가에 담아 모든 일자리를 반환하도록 하기. (수정 1단계 보러 가기.)
