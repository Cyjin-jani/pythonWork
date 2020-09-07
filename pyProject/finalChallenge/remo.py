import requests
from bs4 import BeautifulSoup

#URL format
#https://remoteok.io/remote-dev+python-jobs

def extract_jobs(keyword):
    jobs_list = []
    url = f"https://remoteok.io/remote-dev+{keyword}-jobs"
    print(f"Scrapping remoteok")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("table", {"id": "jobsboard"}).find_all("tr", {"class": "job"})

    for result in results:                 
      job = extract_job_detail(result)
      #print(job)
      jobs_list.append(job)
    return jobs_list

def extract_job_detail(html):
    #print("start extracting details")
    title = html.find("td", {"class":"company position company_and_position"}).find("h2").string
    company = html.find("td", {"class":"company position company_and_position"}).find("h3").string
    link = html.find("td", {"class":"company position company_and_position"}).find("a", {"itemprop": "url"})["href"]

    return {
        'title': title,
        'company': company,
        'link': f"https://remoteok.io/{link}"
    }

def search_jobs(keyword):
  jobs_list = extract_jobs(keyword)
  return jobs_list