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
