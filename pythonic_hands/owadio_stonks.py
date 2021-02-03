def buy_stonks(user_id, stonk_price, wallet, s):
	print('How many stonks would you like to purchase?')
	a = input()
	if a.isdigit() and int(a)*stonk_price <= wallet:
		print('Are you absolutely sure?')
		b = input()
		if b == 'Yes':
			change_field(user_id, 'stonks_count', (int(a)))
			change_field(user_id, 'curr_balance', -(int(a)*stonk_price))
			print(f"Bought {a} stonks at {stonk_price} for a total of {a*stonk_price}.")

def sell_stonks(user_id, stonk_price, wallet, s):
	print('How many stonks would you like to sell?')
		a = input()
		if a.isdigit() and int(a) <= stonks_count:
			print('Are you absolutely sure?')
			b = input()
			if b == 'Yes':
				change_field(user_id, 'stonks_count', -(int(a)))
				change_field(user_id, 'curr_balance', (int(a)*stonk_price))
				print(f"Sold {a} stonks at {stonk_price} for a total of {a*stonk_price}.")



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
		buy_stonks(user_id, stonk_price, wallet, s)

	# Sell stonks code
	if input() == sellstonk:
		sell_stonks(user_id, stonk_price, wallet, s)
		
		# javier hands to change in the future, ideally ask for input again
		# input validity not done, and a "fuck go back" option not done
stonks()
