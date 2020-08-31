import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

companies_list = {}

#get company's list(name and URL) from the home page of alba.co.kr
def get_companies_list():
  company_list = {}
  result = requests.get(alba_url)
  soup = BeautifulSoup(result.text, 'html.parser')
  companies_li = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li")
  
  #find the link and company's name and save it in dictionary
  for company in companies_li:
    company_url = company.find("a", {"class": "goodsBox-info"})["href"]
    company_name = company.find("span", {"class": "company"}).string
    #save datas in company_list
    company_list[company_name] = company_url
  
  #print(company_list)
  return company_list

#extracting details of job information on the each URL
def extract_jobs(url=""):
  job_detail_list = []
  no_jobs = True
  
  #URL check
  if url == "":
    print("no valid url")
    return
  
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_list = soup.find("div", {"id":"NormalInfo"}).find("tbody").find_all("tr")
  
  #check if there is no details of job information, return nothing
  for no_job in job_list:
    nope = no_job.find("td").string  
    if nope == "해당 조건/분류에 일치하는 채용정보가 없습니다.":
      no_jobs = False
  
  if no_jobs == False:
    return      
  
  #extracting job's details
  print(f"start extracting jobs from{url}")
  for i, job in enumerate(job_list):
    if i % 2 == 0:
      job_local = job.find("td", {"class": "local"}).get_text()  
      job_title = job.find("td", {"class": "title"}).find("span", {"class": "title"}).string
      job_time = job.find("td", {"class": "data"}).string
      job_pay = job.find("td", {"class": "pay"}).find_all("span")
      job_date = job.find("td", {"class": "regDate last"}).string

      job_detail_list.append({"local": job_local.replace("\xa0", " "), "title": job_title, "time" : job_time, "pay": job_pay[0].string + job_pay[1].string, "date" : job_date})

  #print(job_detail_list)
  print(f"end extracting jobs from{url}")

  return job_detail_list

#create csv file and input datas
def save_CSV(jobs, file_name):
  print(f"start saving {file_name}information to csv")
  file = open(f"{file_name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for job in jobs:
    writer.writerow(list(job.values()))
  print(f"end saving {file_name}information to csv")  
  return
  
  
def main():
  #get company name and url
  companies_list = get_companies_list()
  #get companies' name only
  company_name_list = list(companies_list.keys())

  for index, company in enumerate(company_name_list):
    print(f"get {company_name_list[index]}'s URL")
    #get company's URL
    url = companies_list[company_name_list[index]]
    #extract the jobs
    jobs = extract_jobs(url)
    #save to csv file when there is job information on the website
    if jobs:
      save_CSV(jobs, company_name_list[index])


main()
