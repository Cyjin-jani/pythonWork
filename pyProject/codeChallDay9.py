import requests
from flask import Flask, render_template, request, redirect

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

#This is Home route
@app.route("/")
def home():
  global news_info
  print("start home")
  orderBy = request.args.get("order_by")
  
  #default order is by "popular"
  if orderBy == None or orderBy == "":
    orderBy = "popular"

  #order by "popular"
  if orderBy == "popular":
    #fake DB check
    existingDB = db.get(orderBy)
    if existingDB:
      article_db = existingDB
    else:  
      article_db = get_popular(popular)
    news_info = get_news_list(article_db)

  #order by "new"
  if orderBy == "new":
    #fake DB check
    existingDB = db.get(orderBy)
    if existingDB:
      article_db = existingDB
    else:  
      article_db = get_new(new)
    news_info = get_news_list(article_db)

  return render_template("index.html", chosenOrder = orderBy, news_list = news_info)

#move to detail pages with article's id (obj_id)
@app.route("/<obj_id>")
def detail(obj_id):
  article_detail = {}
  #obj_id check
  if obj_id == None or obj_id == "favicon.ico":
    print("No obj_id")
    return redirect("/")

  #get the information of article
  for val in news_info:
    if val.get("objectID") == obj_id:
      article_detail = val
      break
     
  #if no article, redirect
  if "objectID" not in article_detail:
    return redirect("/")

  #get the comments info
  comments_list = get_comments_details(obj_id)
  
  return render_template("detail.html", objID = obj_id, article_info = article_detail, comments = comments_list)


#get popular news and make "popluar" fakeDB
def get_popular(url):
  articles = requests.get(url)
  news_info = articles.json()
  db["popular"] = news_info
  article_db = db["popular"]
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
  for datas in article_list:
    news_list.append({
      "title": datas.get("title"), 
      "url": datas.get("url"),
      "points": datas.get("points"),
      "author": datas.get("author"),
      "num_comments": datas.get("num_comments"),
      "objectID": datas.get("objectID")
      })
     
  return news_list


#get the comments data
def get_comments_details(obj_id):
  url = make_detail_url(obj_id)
  comments_info = requests.get(url).json()
  child_list = comments_info["children"]
  comments_list = []  
  for data in child_list:
    comments_list.append({
      "author": data.get("author"),
      "text": data.get("text")
      })

  return comments_list 


app.run(host="0.0.0.0")