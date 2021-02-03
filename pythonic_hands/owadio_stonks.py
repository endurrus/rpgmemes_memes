import math

def stonks(user_id):
	# Display price of stonks for today comparative to ytd.
	# Prompt Buy or Sell stonks
	# Buy -> How many? -> Check if bank balance can afford -> Buy 'how many' at price 'how much? -> buy, database update
	# Sell -> How many -> Sell "How many" at price "How many"? - > sell, database update
	s = get_field('stonks_count')	
	wallet = get_field('curr_balance')
	stonk_price = get_field('')
	print(stonk_price)
	buystonk = 'Buy'
	sellstonk = 'Sell'
	
	# Buy stonks code 
	if input() == buystonk:
	  print('Buy how many? ')
	  a = input()
	  if a.isdigit() and int(a)*stonk_price <= wallet:
	    print('Cfm want Buy?')
	    b = input()
	    if b == 'Yes':
	      change(user_id, 'stonks_count', +(int(a)))
	      change(user_id, 'curr_balance', (int(a)*int(b)))
	      print(f"Bought {a} stonks at {stonk_price} for a total of {a*b}.")
      else:
        break
    else:
      break
  else:
    break

  # Sell stonks code
  if input() == sellstonk:
    print('Sell how many?')
	  a = input()
	  if a.isdigit() and int(a)*stonk_price <= stonks_count:
	    print('Cfm want Sell?')
	    b = input()
	    if b == 'Yes':
	      change(user_id, 'stonks_count', -(int(a)))
	      change(user_id, 'curr_balance', (int(a)*int(b)))
	      print(f"Sold {a} stonks at {stonk_price} for a total of {a*b}.")
      else:
        break
    else:
      break
  else:
    break
  # javier hands to change in the future, ideally ask for input again
stonks()