#Check if input day is on the list or not
def is_on_list(list, day):
  #variable for check
  #(true : on the list, false: not on the list)
  on_list = False
  
  #Using Common Sequence Operation
  if day in list:
    on_list = True

  #other solution
  #compare each element on the list with input data(day)
  """
  for day_in_list in list :
    if day_in_list == day:
      on_list = True
  """
  return on_list

#Check the number of element
def get_x(list, num):
  return list[num]

#Add element
def add_x(list, element):
  list.append(element)

#Remove element
def remove_x(list, element):
  list.remove(element)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
