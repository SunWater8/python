print("==============================")
print("2.0 What is Web Scrapping")
# scrapping이란 url이 가지고 있는 정보를 가지고 관련 preview이미지를 보여주도록 하는 기능
# 10초마다 동일 제품의 가격을 다른 마켓마다 비교하는 기능도 여기에 해당.

print("==============================")
print("2.1 What are We Building")
# 개발자 직업을 stack over flow 사이트에서 검색하면 직업을 구하는 회사의 취업 정보를 볼 수 있다. 
# 이 정보들을 엑셀로 가져와 정리하는 것을 실습해 볼 것이다.

print("==============================")
print("2.2 Navigating with Python")
# indeed와 stackoverflow라는 구인구직사이트에서 검색 결과를 하나의 엑셀 시트로 가져오는 작업 해보기.

"""
1. 웹사이트 들어가기. (https://kr.indeed.com/)
2. 몇개의 페이지가 있는지 확인하기
3. 페이지 하나씩 들어가보기
4. 상세검색으로 검색할 수도 있다.

python requests 패키지 다운받아 import 하기.
python requests 란? : 파이썬에서 요청을 만드는 기능을 모아 놓은 것

 repl.it의 packages 다운 받는 곳에 들어가 requests: Python HTTP for humans를 선택하여 다운받기.
 py파일에 import requests 라고 첫 줄에 입력하고 https://github.com/psf/requests 에서 관련 문장 가지고 오기.


"""

# indeed 사이트에서 python이라고 검색한 결과를 가져와보기. (검색 결과 개수와 검색 결과  html)
import requests

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50") # indeed에서 python을 검색했을 때 나오는 url

print(indeed_result) # <Response [200]>
# print(indeed_result.text) # 모든 html을 가져옴. 여기서 필요한 정보를 가지고 와야 한다. (필요한 정보: 페이지 숫자들... 이 정보는 beautifulsoup 이라는 곳에서 가져올 수 있다. --> https://www.crummy.com/software/BeautifulSoup/)
"""
beautiful soup 은 html에서 정보를 추출하기에 정말 유용한 package(라이브러리)이다. 이 package를 사용하기 위해서는 repl.it에서 다운을 받으면 된다.
(beautifulsoup4:screen scrapping library 라고 검색한 것을 다운받기)
"""



print("==============================")
print("2.3. Extracting Indeed Pages")
# indeed 사이트의 검색결과에 대한 페이지를 배열로 추출하기.

"""
beautiful soup 사이트에서 Documentation 링크 클릭 --> Quick start의 두 번째 참고하기 (첫 번째는 html을 가져오는 거 먼저 했었음.)
"""

import requests
from bs4 import BeautifulSoup #BeautifulSoup 라이브러리 가지고 오기.

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")

# beautifulSoup을 위한 변수 만들기. 이 변수를 가지고 이제 필요한 정보(페이지, 제목이름 등)를 찾을 수 있다. (예: soup.title)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser') # beautifulSoup 사이트에서 quick start 두 번째 내용 참고. soup = BeautifulSoup(html_doc, 'html.parser') 라고 쓰여진 문장 참고.

"""
print(indeed_soup) # indeed의 검색결과에 대한 html을 모두 출력한다. 이 안에 페이지 html을  찾으면 됨.
"""

# <div class="pagination">라고 되어 있는 부분 안에 페이지 숫자가 들어 있기 때문에 이 div를 추출하도록 하기.
pagination = indeed_soup.find("div", {"class":"pagination"})

"""
print(pagination) #pagination 클래스에 해당하는 html만 출력 됨.
"""

# pagination에서 이제 페이지를 가져오기 위해서 a태그만 추출하기.
pages = pagination.find_all('a')

"""
print(pages)
"""

# 리스트를 만들어서 리스트에 있는 각 anchor의 span을 찾아보도록 하기.
"""
for page in pages:
    print(page.find("span"))
"""

# 배열에다가 저장하기.
spans = []
for page in pages:
    spans.append(page.find("span"))

print(spans[:-1]) # [0:-1]는 spans 배열에서 마지막 item을 지칭한다. 마지막 item은 '다음'을 표시한 것이라서 spans 배열에서 제외시킨다.
# [<span class="pn">2</span>, <span class="pn">3</span>, <span class="pn">4</span>, <span class="pn">5</span>]



# 정리해보기 (변수 이름 바꿈. spans->links, spans->pages, page->link)
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50")
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links:
    pages.append(link.find("span"))

print(links)
# 정리 끝


print("==============================")
print("2.4 Extracting Indeed Pages part Two")
# span안의 text만 가지고 오기
for link in links:
    pages.append(link.find("span".string))

print(links[:-1]) # 