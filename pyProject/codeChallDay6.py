import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

#An array that has the name of the country and the "Alpha-3 code"
countries = []

#save country
country_a = ""
country_b = ""

def main():
  global countires
  global country_a
  global country_b
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

  #Check the input and save country
  print("Where are you from? Choose a country by number.")
  country_a = check_answer()
  print("Now choose another country.")
  country_b = check_answer()
  #get the code
  convert_list = get_country_code(country_a, country_b)
  #get amount to convert
  amount = get_amount() 
  #convert Currency
  convert_currency(convert_list, amount)
  

#Show the list of countries
def print_country_list():
  print("Welcome to Currency Convert pro 2020")
  list_index = 0
  for name, code in countries:
    print(f"# {list_index} {name}")
    list_index = list_index + 1

#Check the input data
def check_answer():
  global countries
  print("# : ")
  try:
    answer = int(input(""))
    if answer > 264 or answer < 0:
      print("Choose a number from the list. ")
      return check_answer()
    else:
      print(f"{countries[answer][0]}")
      return answer
  except:
    print("That was not a number.")
    return check_answer()

#Show country's code
def get_country_code(country_a, country_b):
  global countries
  print(f"How many {countries[country_a][1]} do you want to convert to {countries[country_b][1]}?")
  return countries[country_a][1], countries[country_b][1]

#get amount to convert
def get_amount():
  print("# : ")
  try: 
    answer = int(input(""))
    return answer
  except:
    print("That was not a number. please try again.")
    return get_amount()

def convert_currency(cur_list, amount):
  global countries
  global country_a
  global country_b
  currency_a = cur_list[0]
  currency_b = cur_list[1]
  URL =f"https://transferwise.com/gb/currency-converter/{currency_a}-to-{currency_b}-rate?amount={amount}"

  try:  
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    rate = soup.find("span", {"class":"text-success"}).text
    
    #Use the 'format_currency' function to format the output of the conversion
    print(f"{currency_a} {amount} is " + format_currency(float(amount) * float(rate), currency_b, locale="ko_KR"))
  
  except:
    print("not supported currency.")
    print("TRY AGAIN")
    countries = []
    country_a = ""
    country_b = ""
    main()


main()  

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""
#Used in 'convert_currency' function above
#print(format_currency(5000, "KRW", locale="ko_KR"))