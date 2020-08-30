#4.1. Flask

from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper") #name of application

#fake DB
db = {}


@app.route("/")
def home():
  return render_template("home.html")

"""
@app.route("/<username>") #<>의 뜻은 placeholder
def contact(username):
  return f"Hello {username}, how are u doing?"
"""

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template(
    "report.html", 
    searchingBy = word, 
    resultsNumber = len(jobs),
    jobs = jobs
  )

app.run(host="0.0.0.0")