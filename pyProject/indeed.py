#외부 url에 접속할 수 있도록 requests라는 라이브러리 임포트
import requests
#html을 보기 쉽게 만들어주는 라이브러리 임포트
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

#indeed의 정보 추출 함수
def get_last_page():
  #url에서 정보 가져오기
  result = requests.get(URL)
  #가져온 정보(text)를 html형식으로 
  soup = BeautifulSoup(result.text, 'html.parser')
  #페이지 정보 찾기
  pagination = soup.find("div", {"class":"pagination"})
  #가지고 있는 페이지를 리스트로
  links = pagination.find_all('a')
  
  #빈 리스트 생성 (페이지 번호가 적힌 span태그들만 모으기 위함)
  pages = []
  #페이지가 써있는 span태그를 추출하여 pages 리스트에 저장 (맨 마지막 제외(next이기 때문))
  for link in links[:-1]:
    pages.append(int(link.string))
    #이 코드 또한 위와 같은 결과가 나옴 pages.append(link.find("span").string)
  
  #맨 마지막 페이지 확인 
  max_page = pages[-1]
  return max_page

def extract_job(html):
      title = html.find("h2", {"class": "title"}).find("a")["title"]
      company = html.find("span", {"class": "company"})
      company_anchor = company.find("a")
      if company :
        if company_anchor is not None:
          company = str(company_anchor.string)
        else:
          company = str(company.string)
        company = company.strip()
      else:
        company = None  
      location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
      job_id = html["data-jk"]
      return {'title': title, 'company': company, 'location': location, 'link': f"https://www.indeed.com/viewjob?=jk={job_id}"}

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    #print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
