y = get_field("curr_energy")
z = get_field("salary_base")
items = get_field("item_list")

if items[0] == '1':
  x = 2
elif items[1] == '1':
  energy_mult = 0.5
elif items[0:2] == '11'
  x = 2
  energy_mult = 0.5
else:
  x = 1
  energy_mult = 1

def wgt_work():
	# When user clicks "work", the user's curr_energy will be deducted by 60 units, max_energy increased by 100 units and curr_balance doubled.
	if y >= 60:
		change(user_id, "curr_energy", (-60 * energy_mult))
		change(user_id, "max_energy", 1)
		change(user_id, "curr_balance", (z * x))
	else:
		pass
		# javier handjob

def wgt_keng():
	# When user clicks "chao keng", the user's curr_energy will be deducted by 20 units.
	if y >= 20:
		change(user_id, "curr_energy", (-20 * energy_mult))
	else:
		pass
		#javier blowblow


def main():
	wgt_work()
	wgt_keng()
	
if__name__ == "__main__":
	main()
	