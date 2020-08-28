import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

#An array that has the name of the country and the "Alpha-3 code"
countries = []

def main():
  global countires
  url = "https://www.iban.com/currency-codes"
  #get information of countries start -----
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  get_list = soup.find("tbody").findAll("td")
  #get information of countries end -----
  country_list = []

  #extract texts from the soup
  for index, td in enumerate(get_list):
    if index % 2 == 0 or index == 0: 
      td = str(td).replace("<td>", "").replace("</td>", "")
      country_list.append(td)
  
  #Make lists and save countries' name and code
  for i, country in enumerate(country_list):
    if i%2 == 0 and i != len(country_list):
      if country_list[i+1] != "":
        countries.insert(i, [country_list[i].lower().capitalize(), country_list[i+1]])
    
  #Show the list of countries
  print_country_list()

  #Check the input and show codes
  show_country_code(check_answer())

#Show the list of countries
def print_country_list():
  print("Hello! Please select a country by number! :")
  list_index = 0
  for name, code in countries:
    print(f"# {list_index} {name}")
    list_index = list_index + 1

#Check the input data
def check_answer():
  print("# : ")
  try:
    answer = int(input(""))
    if answer > 264 or answer < 0:
      print("Choose a number from the list. ")
      return check_answer()
    else:
      return answer
  except:
    print("That was not a number.")
    return check_answer()

#Show country's code
def show_country_code(num):
  global countries
 
  print(f"You chose {countries[num][0]}.")
  print(f"The currency code is {countries[num][1]}.")


main()  