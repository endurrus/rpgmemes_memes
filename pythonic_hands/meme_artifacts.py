x = get_field(user_id, "meme_list")
y = get_field(user_id, 'item_list')
d = [500000,250000,100000,15,10000,1,500000]

def meme_artifacts(user_id):
  bal = get_field(user_id, "curr_balance")
  # Display prices of the meme artifacts and their respective rewards (meme_cost, message, changes to curr_energy, salary_base and max_energy)
  if d[a]>bal:
    print("You can't afford this. Work harder, bro.")
    
  elif a == 0:
    change_field(user_id, 'meme_list', 0, '1')
    print('DART training:')
    print('Obtain relevant essential cyber skills.')
    
  elif a == 1:
    change_field(user_id, 'meme_list', 1, '1')
    print('CPT Kester Neo cosplay:')
    print('Chao geng is now secret.')
    print('Lol no.')
    
    elif a == 2:
    change_field(user_id, 'meme_list', 2, '1')
    change_field(user_id, 'max_energy', get_field(user_id, 'max_energy'))
    change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
    print("Ex Chao Keng")
    
  elif a == 3:
    change_field(user_id, 'meme_list', 3, '1')
    change_field(user_id, 'max_energy', 10)
    print("Eng Chun's CNY snacks")
    
  elif a == 4:
    change_field(user_id, 'meme_list', 4, '1')
    if y[5] == '1':
      change_field(user_id, 'item_list', 5, '0')
    else:
      change_field(user_id, 'max_energy', 100)
    print('CWC deproved')
      
  elif a == 5:
    change_field(user_id, 'meme_list', 5, '1')
    print("Jeff's long-lost map.")
    print("Gained profound knowledge on SolarWinds Exploitation and how Cyber Kill Chain works.")
    print("+7 extra")
    
  elif a == 6:
    change_field(user_id, 'meme_list', 6, '1')

    
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
