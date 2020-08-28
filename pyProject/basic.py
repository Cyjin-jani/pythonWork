from math import ceil, fsum as good_sum
from calculator import plus as imported_plus

a_string = "like this"
a_boolean = True
a_number = 2
a_float = 3.12
a_None = None

#print(type(a_None))

#about list (mutable Sequence)
days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

#print(days[2])
#print(len(days))
#print("Mon" in days)

days.append("Sun")
days.reverse()
#print(days)

#immutable Sequences (tuple)

day_of_week = ("Mon", "Tue", "Wed", "Thr", "Fri", "Sat")
#print(type(day_of_week))

#dictionary

me = {"name": "yj", "age": 29, "fav_food": ["kimchi", "gogi"], "Korean": True, "tutu": ("t", "p")}

#print(me)

me["handsome"] = True

#print(me)

# function


def say_hello(who):
  #print("HELLO", who)
  hi = who + ""
  #print(hi)

say_hello("nico")

def plus_number(a, b):
  print(a + b)

#plus_number(2, 5)

def minus(a, b=0):
  print(a - b)

#minus(2)
#minus(5, 2)


def p_plus(a, b):
  print(a+b)

def r_plus(a, b):
  return a + b

#p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

#print (p_result, r_result)

result_plus = r_plus(b=30, a=1)
#print(result_plus)

#keyword argument
def say_hi(name, age):
  return f"Hello {name} you are {age} years old"

hello = say_hi(age="12", name="john")
#print(hello)

# if - else statement

def func_plus(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None

#print(func_plus(12, "10"))
#print(func_plus(12, 1.2))


def age_check(age):
  #print(f"you are {age}")
  if age < 18:
   print("you cannot drink")
  elif age == 18:
    print("you are new to this!")
  elif age > 20 and age < 25:
    print("you are still kind of young~!")    
  else:
    print("enjoy drinks")  

#age_check(29)


days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for day in days:
  if day == "Wed":
    break
  else:  
    #print(day)
    break

for number in [1,2,3,4,5]:
   print(number)

for letter in "example":
   print(letter)


# about module
print(ceil(1.2))
print(good_sum([1, 2, 3, 4, 5, 6, 7]))


print(imported_plus(1, 2))
