"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file

from so import search_jobs as so_get_job
from wework import search_jobs as wew_get_job
from remo import search_jobs as remo_get_job
from exporter import save_to_file

app = Flask("RemoteWorkScrapper") #name of application

#fake DB
db = {}
total_list = []
total_res_num = 0

#go to home page
@app.route("/")
def home():
  return render_template("home.html")

#search and show result on details page
@app.route("/goSearch")
def goSearch():
  word = request.args.get('word')
  if word:
    word = word.lower()
    #DB Check
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    #extract jobs
    else:
      jobs = so_get_job(word) + wew_get_job(word) + remo_get_job(word)
      db[word] = jobs
  else:
    return redirect("/")

  return render_template("details.html", jobsList = jobs, results_num = len(jobs), searchingBy = word)

#export to csv
@app.route("/goExport")
def goExport():
  try:
    word = request.args.get('word')
    #word check
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    # result check
    if not jobs:
      raise Exception() 
    #export to csv file
    save_to_file(word, jobs)  
    return send_file(f"{word}.csv")
  except:  
    return redirect("/")


app.run(host="0.0.0.0")  