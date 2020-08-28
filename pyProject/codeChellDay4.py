import os
import requests

#restart check variable
try_again = True

#Make a list of URLs and Check the code of Url
def check_input_URL(input_url):
  results = []
  #change to lowerCase
  input_url = input_url.lower()
  #make a list of urls
  input_urls = input_url.split(',')
  
  #remove spaces
  for urls in input_urls:
    results.append(urls.strip())

  #Check the 'http'keyword
  i = 0
  for url in results:
    if "http" not in url :
      url = "http://" + url
      #print(url)
    
    results[i] = url
    i = i + 1 

  #Check the status_code of url
  for url in results:
    try:
      s_code = requests.get(url).status_code
          
    except:
      print(f"{url} is not a valid url. please try again.")
      return

    if s_code == 200:
        print(f"{url} is up!")
    else:
        print(f"{url} is Down!")   

#Ask if the user wants to restart program or not
def start_over():
  global try_again
  restarts = input("Do you want to start over? y/n ").lower()
  if restarts == "y":
    try_again = True
  elif restarts == "n":
    print("ok, Bye!")
    try_again = False
  else:
    print("not a valid answer")
    start_over()

#Run the program
while (try_again):
  #clear
  os.system('clear')

  #Announcement
  print("HELLO! Welcome to IsItDown.py!")
  print("please write a URL / URLs you want to check. (seperated by comma) ")

  #get user's input
  get_url = input()
  
  #Check the urls' status_code
  check_input_URL(get_url)
  
  #Check the program restart 
  start_over()
