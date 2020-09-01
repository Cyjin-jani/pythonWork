import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")
news_info = []

@app.route("/")
def home():
  global news_info
  print("start home")
 
  orderBy = request.args.get("order_by")
  if orderBy == None:
    orderBy = "popular"
  
  if orderBy == "popular":
    existingDB = db.get(orderBy)
    if existingDB:
      article_db = existingDB
    else:  
      article_db = get_popular(popular)
    news_info = get_news_list(article_db)

  if orderBy == "new":
    existingDB = db.get(orderBy)
    if existingDB:
      article_db = existingDB
    else:  
      article_db = get_new(new)
    news_info = get_news_list(article_db)


  return render_template("index.html", chosenOne = orderBy, news_list = news_info)

#move to detail pages
@app.route("/<obj_id>")
def detail(obj_id):
  article_detail = {}  
  #get the information of article
  for val in news_info:
    if val.get("objectID") == obj_id:
      article_detail = val
      break

  #get the comments info
  url = make_detail_url(obj_id)
  comments_info = requests.get(url).json()
  child_list = comments_info["children"]

  comments_list = []  
  for data in child_list:
    comments_list.append({
      "author": data.get("author"),
      "text": data.get("text")
      })
  
  
  return render_template("detail.html", objID = obj_id, article_info = article_detail, comments = comments_list)



#get popular news and make "popluar" fakeDB
def get_popular(url):
  articles = requests.get(url)
  news_info = articles.json()
  db["popular"] = news_info
  article_db = db["popular"]
  
  #print(article_list[0])
  return article_db

#get the newest news and make "new" fakeDB
def get_new(url):
  articles = requests.get(url)
  news_info = articles.json()
  db["new"] = news_info
  article_db = db["new"]
  
  return article_db

#get real news information and save it on the list
def get_news_list(article_db):
  article_list = article_db["hits"]
  news_list = []
  
  for i, check in enumerate(article_list):
    news_list.append({
      "title": check.get("title"), 
      "url": check.get("url"),
      "points": check.get("points"),
      "author": check.get("author"),
      "num_comments": check.get("num_comments"),
      "objectID": check.get("objectID")
      })
     
  return news_list



def get_details(id_list):
  
  #for id in id_list:
  #  detail_url = make_detail_url(id)
  #  detail_info = request.get(detail_url).json()
  detail_url = make_detail_url(id_list[0])
  detail_info = requests.get(detail_url).json()
  #print(detail_info)




app.run(host="0.0.0.0")