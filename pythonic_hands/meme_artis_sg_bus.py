a = get_field(user_id, "meme_list")
y = get_field(user_id, 'item_list')
d = [500000,250000,100000,15,10000,1,500000]

def message0():
 if a == 0:
  print('DART training: \nTo obtain essential cyber skills')
    else:
     pass

def message1():
 if a == 1:
  print("CPT Kester Neo cosplay: \nChao Keng is now secret. \n'Lol no.' \nEx CHAOKENG")
 else:
  pass

def message2():
 if a == 3:
  print("Eng Chun's CNY snacks")
 else:
  pass

def message3():
 if a == 4:
  print('CWC deproved')
 else:
  pass
 
def message5():
 if a == 5:
  print("Jeff's long-lost map. \nGained profound knowledge on SolarWinds Exploitation and how Cyber Kill Chain works. \n+7 extra")
 else:
  pass

def message6():
 if a == 6:
  print("I'm ME4T Keith Chan!")
 else:
  pass
  
def meme_artifacts(user_id):
  b = get_field(user_id, "curr_balance")
  # Display prices of the meme artifacts and their respective rewards (meme_cost, message, changes to curr_energy, salary_base and max_energy)
 if d[a]>b:
     print("You can't afford this. Work harder, bro.")
    
 elif a == 0:
     change_field(user_id, 'meme_list', 0, '1')
     message0()
    
 elif a == 1:
     change_field(user_id, 'meme_list', 1, '1')
     message1()
    
 elif a == 2:
     change_field(user_id, 'meme_list', 2, '1')
     change_field(user_id, 'max_energy', get_field(user_id, 'max_energy'))
     change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
     message2()
    
 elif a == 3:
  change_field(user_id, 'meme_list', 3, '1')
  change_field(user_id, 'max_energy', 10)
  message3()
 
 elif a == 4:
  change_field(user_id, 'meme_list', 4, '1')
  if y[5] == '1':
    change_field(user_id, 'item_list', 5, '0')
  else:
    change_field(user_id, 'max_energy', 100)
  message4()
   
 elif a == 5:
  change_field(user_id, 'meme_list', 5, '1')
  message5()
  
 elif a == 6:
  change_field(user_id, 'meme_list', 6, '1')
  message6()
 else:
  pass
 
 if y[3] != '1':
   change_field(user_id, 'item_list', 3, '1')
   change_field(user_id, 'salary_inc', 500)
 elif y[5] != '1':
   change_field(user_id, 'item_list', 5, '1')
   change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
 elif y[7] != '1':
   change_field(user_id, 'item_list', 7, '1')
   change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
   
 print("I'm ME4T Keith Chan!")
 else:
  pass
# need to pop off dictionary if meme bought
# javier hands to change in the future, ideally ask for input again
meme_artifacts()
