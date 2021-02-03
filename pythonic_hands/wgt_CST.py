import random
import numpy as np
import random

def wgt_cst(user_id):
  if get_field(user_id, "curr_energy") >= 40:
    change_field(user_id, "curr_energy", -40)
    gacha(user_id, get_field(user_id, 'item_list'))
  else:
  '''javier's handjob time'''
    pass
    
def gacha(user_id, item_list):
  list1 = ['Pythonic Hands', 'Computational Genius', 'SMS Scholar']
  list2 = ['Loyalty to Country', 'Leadership', 'Discipline', 'Proffessionalism', 'Fighting Spirit', 'Ethics', 'Care for Soldiers', 'Safety']
  d = {'SSR' : list1, 'SR' : list2}
  items = ['SSR', 'SR', "Guess I'll study again another time!"] # Item list
  prob = [0.5, 0.49, 0.01] # list of probabilities (sum should be 1)
  N = 1 # Number of draws, always 01
  #Lottery
  result = (np.random.choice(items, p=prob))
  
  if result == "SSR":
    a = random.randint(0, len(list1)-1)
    if item_list[a] == '1':
      return gacha(user_id, item_list)
      
    else:
      print(a) # BINARY INT THAT NEEDS TO BE CHANGED
      print(d[result][a]) # PRIZE WON, PRINT IT OUT, javier
      change_field(user_id, 'item_list', a, '1')
      if a == 2:
        change_field(user_id, 'salary_inc', 1500)
      
  elif result == "SR":
    a = random.randint(0, len(list2)-1)
    if item_list[a+3] == '1':
      return gacha(user_id, item_list)

    else:
      print(3+a) # BINARY INT THAT NEEDS TO BE CHANGED
      print(d[result][a]) # PRIZE WON, PRINT IT OUT, javier
      change_field(user_id, 'item_list', 3+a, '1')
      if a == 0:
        change_field(user_id, 'curr_balance', 30000)
      elif a == 1:
        change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
      elif a == 2:
        change_field(user_id, 'max_energy', 50)
      elif a == 3:
        change_field(user_id, 'salary_inc', 500)
      elif a == 4:  
        change_field(user_id, 'max_energy', 50)
      elif a == 5:
        change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
      elif a == 6:
        # Cron job, salary increment every 5 days
      elif a == 7:
        change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
  
  else:
    # print result, nothing happens
    print(result)
    # javier blowjob
    # more or less done, left implementation