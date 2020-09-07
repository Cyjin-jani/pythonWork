import requests
from bs4 import BeautifulSoup

#URL format
#https://weworkremotely.com/remote-jobs/search?term=python

def extract_jobs(keyword):
    jobs_list = []
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
    print(f"Scrapping wework")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div", {"class": "jobs-container"}).find_next("section", {"class": "jobs"}).find("ul").find_all("li", {"class": "feature"})

    for result in results:
            job = extract_job_detail(result)
            jobs_list.append(job)  
    return jobs_list

def extract_job_detail(html):
    #print("start extracting details")
    title = html.find("span", {"class":"title"}).string
    company = html.find("span", {"class":"company"}).string
    a_tag = html.find_all("a")
    for a in a_tag:
      if a.find("span", {"class":"company"}) != None:
        link = a["href"]
        break
    
    return {
        'title': title,
        'company': company,
        'link': f"https://weworkremotely.com{link}"
    }

def search_jobs(keyword):
  jobs_list = extract_jobs(keyword)
  return jobs_list