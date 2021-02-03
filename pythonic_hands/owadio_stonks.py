def stonks(user_id):
	# Display price of stonks for today comparative to ytd.
	# Prompt Buy or Sell stonks
	# Buy -> How many? -> Check if bank balance can afford -> Buy 'how many' at price 'how much? -> buy, database update
	# Sell -> How many -> Sell "How many" at price "How many"? - > sell, database update
	s = get_field(user_id, 'stonks_count')	
	wallet = get_field(user_id, 'curr_balance')
	stonk_price = get_field('')
	buystonk = 'Buy Stonks'
	sellstonk = 'Sell Stonks'
	
	# Buy stonks code 
	if input() == buystonk:
	  print('Buy how many?')
	  a = input()
	  if a.isdigit() and int(a)*stonk_price <= wallet:
	    print('Cfm want Buy?')
	    b = input()
	    if b == 'Yes':
	      change_field(user_id, 'stonks_count', (int(a)))
	      change_field(user_id, 'curr_balance', -(int(a)*int(b)))
	      print(f"Bought {a} stonks at {stonk_price} for a total of {a*b}.")

	# Sell stonks code
	if input() == sellstonk:
		print('Sell how many?')
		a = input()
		if a.isdigit() and int(a)*stonk_price <= stonks_count:
			print('Cfm want Sell?')
			b = input()
			if b == 'Yes':
				change_field(user_id, 'stonks_count', -(int(a)))
				change_field(user_id, 'curr_balance', (int(a)*int(b)))
				print(f"Sold {a} stonks at {stonk_price} for a total of {a*b}.")
      
		# javier hands to change in the future, ideally ask for input again
		# input validity not done, and a "fuck go back" option not done
stonks()
