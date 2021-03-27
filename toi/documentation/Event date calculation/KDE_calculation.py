months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def date_calc(event_year, event_month, event_date, start_year = 1858, s_m = 1, s_d = 1):
	year = event_year-start_year
	month = s_m
	date = event_date-s_d

	if month > event_month:
		year -= 1
	days = 0
	while month != event_month:
		days += months[month]
		if month == 12:
			month = 1
		else:
			month += 1
	
	days += year*365+date # Convert a date into days

	print("\nEvent start: days =", int(days)) # Print out days

	if start_year >= 1858: # If event is fired in 1857 we should put it in _on_startup_events
		print("Should be put inside KDE_bi_yearly_event_fire_" + str(start_year) + "_to_" + str(start_year+1) + ".")
	elif start_year == 1857:
		print("Should be put into _on_startup_events.txt.")
	else:
		print("Error: Invalid date. Should be after 1857 05 11.")

	print("\nIf you want to add randomization you may add random_days = [days] to country_event.\n")

while True:
	event_date = [int(x) for x in input("Enter the date around which you want to receive the event (YYYY MM DD, separated by spaces):").split()] # Get provided date as a string and convert to an int array
	year = event_date[0]
	month = event_date[1]
	date = event_date[2]

	if year == 1857:
		date_calc(year, month, date, 1857, 5, 11)
	elif year % 2 == 0: # If the year is an even number.
		date_calc(year, month, date, year)
	else:
		date_calc(year, month, date, year-1) # Subtract one year if it is a odd number
