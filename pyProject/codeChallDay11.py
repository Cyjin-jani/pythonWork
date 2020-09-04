import requests
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""
baseURL = "https://www.reddit.com/r/"
subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")

#get articles' detail information
def get_articles(subreddit):
  url = f"{baseURL}{subreddit}/top/?t=month"
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  detail_info = soup.find_all("div", {"class":"Post"})
  
  article_list = []

  for i, data in enumerate(detail_info):
    #ignore the advertisement info
    if i == 1: 
      pass
    #for exceptional case of flutter  
    elif subreddit == "flutter" and i == 2:
      pass  
    else:
      #extract datas
      try:
        res_title = data.h3.find(string=True)
        res_link = "https://www.reddit.com" + data.find("a", {"data-click-id":"body"})["href"]
        res_vote = data.find("button", {"data-click-id":"upvote"}).find_next("div").string
        #reform over 1000 votes (ex 1.2k -> 1200)
        if 'k' in res_vote:
          res_vote = res_vote.replace("k", "")
          res_vote = float(res_vote) * 1000

      except:
        print("SUBREDDIT: ", subreddit, res_title, res_link, res_vote)
        return redirect("/")

      #make a list of articles
      article_list.append({
        "title" : res_title,
        "link" : res_link,
        "vote" : int(res_vote),
        "subject":"r/"+subreddit
      })

  return article_list

#go home page
@app.route("/")
def home():
  print("start home")
  return render_template("home.html")

#go read(details) page
@app.route("/read")
def read():
  print("go read")
  #list for checking what user checked
  checked_list = []
  #article's list
  results_list = []

  #check the subreddits
  for subred in subreddits:
    result = request.args.get(subred)
    if result == None:
      pass
    elif result == 'on':
      #get the articles' info
      results_list.extend(get_articles(subred))
      checked_list.append("r/"+subred) 

  #if there is no selected one, redirect home
  if len(checked_list) < 1:
    return redirect("/")

  #re-sort (asc)
  for index in range(len(results_list)):
    for i in range(len(results_list)- index):
      if i+1 < len(results_list):
        if results_list[i]["vote"] > results_list[i+1]["vote"]:
          temp = results_list[i+1]
          results_list[i+1] = results_list[i]
          results_list[i] = temp 

  results_list = reversed(results_list)
  article_info = list(results_list)
  
  return render_template("read.html", subred_list = checked_list, article_list = article_info)  

app.run(host="0.0.0.0")