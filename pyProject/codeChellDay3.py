#common function for checking the dictionary
def check_the_dict(ch_dict):
  check_type = True
  type_dict = type(ch_dict)
  if type_dict != type({}):
    print(f"You need to send a dictionary. You sent: {type_dict}")
    check_type = False
  return check_type


def add_to_dict(p_dict={}, word="", scripts=""):
  #Check the type of first argument
  if check_the_dict(p_dict) is not True:
    return
  #Check the definition is not empty
  if scripts == "" or word == "":
    print("You need to send a word and a definition.")
    return
  #Check the word is already added on the dictionary  
  if word in p_dict:
    print(f"{word} is already on the dictionary. Won't add.")
    return
  #Add the word and definition on the dictionary  
  p_dict[word] = scripts
  print(f"{word} has been added.")

  return 

def get_from_dict(p_dict={}, word=""):
  #Check the type of first argument
  if check_the_dict(p_dict) is not True:
    return
  #Check the keyword is not empty
  if word == "":
    print("You need to send a word to search for.")
    return
  #Check and print if the word is in the dict 
  if word in p_dict:
    print(f"{word}: {p_dict[word]}")
    return
  else:
    print(f"{word} was not found in this dict.")
  
  return     


def update_word(p_dict={}, word="", scripts=""):
  #Check the type of first argument
  if check_the_dict(p_dict) is not True:
    return
  #Check the definition is not empty
  if scripts == "":
    print("You need to send a word and a definition to update.")
    return  
  #Check and update if the word is in the dict 
  if word in p_dict:
    p_dict[word] = scripts
    print(f"{word} has been updated to: {p_dict[word]}")
    return
  else:
    print(f"{word} is not on the dict. Can't update non-existing word.")
  return

def delete_from_dict(p_dict={}, word=""):
  #Check the type of first argument
  if check_the_dict(p_dict) is not True:
    return
  #Check the keyword is not empty
  if word == "":
    print("You need to specify a word to delete.")
    return
  #Check and delete if the word is in the dict 
  if word in p_dict:
    del p_dict[word]
    print(f"{word} has been deleted.")
    return
  else:
    print(f"{word} is not in this dict. Won't delete.")
  return



import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")
