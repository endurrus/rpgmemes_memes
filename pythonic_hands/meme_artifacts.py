import math

if __name__ == "__main__":
  a = input()  

x = get_field(user_id, "meme_list")
y = get_field(user_id, 'item_list')

d = { 'Meme_Artifact #1' : [500000], 'Meme_Artifact #2' : [250000], 'Meme_Artifact #3' : [100000], 'Meme_Artifact #4' : [15], 'Meme_Artifact #5' : [10000], 'Meme_Artifact #6' : [1], 'Meme_Artifact #7' : [500000]
}


def meme_artifacts(user_id):
  # Display prices of the meme artifacts and their respective rewards (meme_cost, message, changes to curr_energy, salary_base and max_energy)
  if a == '1':
    change_field(user_id, 'meme_list', 0, '1')
    print('DART training:')
    print('Obtain relevant essential cyber skills.')
  elif a == '2':
    print('CPT Kester Neo cosplay:')
    print('Chao geng is now secret.')
    print('Lol no.')
    change_field(user_id, 'meme_list', 1, '1')
  elif a == '3':
    change_field(user_id, 'meme_list', 2, '1')
    change_field(user_id, 'max_energy', 2)
    change_field(user_id, 'salary_base', get_field(user_id, 'salary_base') * 0.5)
    print("Eng Chun's CNY snacks")
  elif a == '4':
    change_field(user_id, 'meme_list', 3, '1')
    change_field(user_id, 'max_energy', 10)
    change_field(user_id, 'meme_list', a, '1')
    print('CWC deproves')
  elif a == '5':
    change_field(user_id, 'meme_list', 4, '1')
    if y[5] == '1':
      change_field(user_id, 'item_list', 5, '1')
    else:
      change_field(user_id, 'max_energy', 100)
  elif a == '6':
    change_field(user_id, 'meme_list', 5, '1')
    print("Jeff's long-lost map.")
    print("Gained profound knowledge on SolarWinds Exploitation and how Cyber Kill Chain works.")
    print("+7 extra")
  elif a == '7':
    change_field(user_id, 'meme_list', 6, '1')
    print("I'm ME4T Keith Chan!")
    change_field(user_id, 'item_list', 3, '1')
    change_field(user_id, 'item_list', 5, '1')
    change_field(user_id, 'item_list', 8, '1')

  else:
    pass
# need to pop off dictionary if meme bought
# javier hands to change in the future, ideally ask for input again
meme_artifacts()
