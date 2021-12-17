# /////////////////////////////////////////////////////////////////
# 코드 정리하기
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}"

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