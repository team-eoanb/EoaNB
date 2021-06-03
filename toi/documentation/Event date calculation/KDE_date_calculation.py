months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Length of each month in days. First one is -1 because arrays start at 0.
def date_calc(event_year, event_month, event_day, start_year = 1858, s_m = 1, s_d = 1):
	year = event_year-start_year
	month = s_m
	day = event_day-s_d

	if month > event_month:
		year -= 1

	days = 0
	while month != event_month: # Add months to days
		days += months[month]
		if month == 12:
			month = 1
		else:
			month += 1

	days += year*365+day # Convert a date into days

	if days < 0 or event_year < 1857: # Prevent negative numbers when providing a date
		print("Error: Invalid date. Should be after 1857 05 11.")
		return

	if event_year >= 1858:
		print("Should be put inside KDE_bi_yearly_event_fire_" + str(start_year))
	else:
		print("Should be put into _on_startup_events.txt.") # If event is fired in 1857 we should put it in _on_startup_events

	print("days =", int(days)) # Print out days


while True:
	event_day = [int(x) for x in input("\n\nEnter the date around which you want to receive the event (YYYY MM DD, separated by spaces):").split()] # Get provided day as a string and convert to an int array
	year = event_day[0]
	month = event_day[1]
	day = event_day[2]

	if year == 1857:
		date_calc(year, month, day, 1857, 5, 11)
	else:
		date_calc(year, month, day, year-year % 2) # If it is an odd number, remove one: 1859 -> 1858.
