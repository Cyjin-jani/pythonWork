import requests
from bs4 import BeautifulSoup

#URL format
#https://stackoverflow.com/jobs?r=true&q=python
def get_url(keyword):
  url = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
  return url

def get_last_page(keyword):
  url = get_url(keyword)
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  try:
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
  except:
    return 1, url  
  last_page = pages[-2].get_text(strip=True)
  return int(last_page), url

def extract_jobs(last_page, url):
    jobs_list = []
    for page in range(last_page):
      print(f"Scrapping so result page : {page}")
      result = requests.get(f"{url}&pg+{page+1}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "-job"})
      
      for result in results:
        job = extract_job_detail(result)
        noData = True
        for data in jobs_list:
          if data["link"] == job["link"]:
            noData = False
            break;
          else:
            noData = True  
        if noData:    
          jobs_list.append(job)

    #print(jobs_list)

    return jobs_list

def extract_job_detail(html):
    #print("start extracting details")
    title = html.find("h2").text.strip()
    company = html.find("h3", {
        "class": "fc-black-700"
    }).find_all(
        "span", recursive=False)[0]
    company = company.get_text(strip=True)
    job_id = html["data-jobid"]
    return {
        'title': title,
        'company': company,
        'link': f"https://stackoverflow.com/jobs/{job_id}",
        'jobID': job_id
    }

def search_jobs(keyword):
  [last_page, url] = get_last_page(keyword)
  jobs_list = extract_jobs(last_page, url)
  return jobs_list