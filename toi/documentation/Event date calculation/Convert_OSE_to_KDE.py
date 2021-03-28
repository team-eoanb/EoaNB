from collections import defaultdict
from pathlib import Path

months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
toi_folder = Path(__file__).parents[2]
f = toi_folder.joinpath("common/on_actions/_on_startup_events.txt")

def reverse_date_calculation(s_y, s_m, s_d, d):
	d += s_d
	e_y = s_y + d // 365
	d = d % 365
	m = s_m
	while d > months[m]:
		d -= months[m]
		if m == 12:
			m = 1
			e_y += 1
		else:
			m += 1
	if d == 0:
		m -= 1
		d = months[m]

	return [e_y, m, d]


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

	if start_year == 1857:
		KDE_scripted_effect = "on_startup"
	else:
 		KDE_scripted_effect = "KDE_bi_yearly_event_fire_" + str(start_year) + "_to_" + str(start_year+1)

	return int(days), KDE_scripted_effect


def parse_line(text):
	text = str(text)
	args = text.split(" ")

	event_type = ""

	if "country_event" in args[0]:
		event_type = "country_event"
	elif "news_event" in args[0]:
		event_type = "news_event"

	random_days = 0
	if "random_days" in text:
		random_days = int(args[11])

	return int(args[8]), event_type, args[5], random_days


lines = f.read_text().splitlines()

from_to = [int(x) for x in input("Line from, and to: ").split(" ")]

scripted_effect_instances = defaultdict(list)

for i in range(from_to[0]-1, from_to[1]):
	line = lines[i]
	if "country_event" in line or "news_event" in line:
		days, event_type, event_id, random_days = parse_line(line)
		date = reverse_date_calculation(1857, 5, 11, days)

		year = date[0]
		month = date[1]
		day = date[2]

		execution_block = ""
		days_from_KDE = 0

		if year == 1857:
			block_year, block_month, block_date = 1857, 5, 11
		elif year % 2 == 0: # If the year is an even number.
			block_year, block_month, block_date = year, 1, 1
		else:
			block_year, block_month, block_date = year-1, 1, 1

		days_from_KDE, KDE_scripted_effect = date_calc(year, month, day, block_year, block_month, block_date)

		if random_days == 0:
			code_string = event_type + " = { id = " + event_id + " days = " + str(days_from_KDE) + " } # " + str(year) + "." + str(month) + "." + str(day)
		else:
			code_string = event_type + " = { id = " + event_id + " days = " + str(days_from_KDE) + " random_days = " + str(random_days) + " } # " + str(year) + "." + str(month) + "." + str(day)

		scripted_effect_instances.setdefault(KDE_scripted_effect, []).append(code_string) # This adds the code to the dictionary


for key, value in scripted_effect_instances.items(): # This prints out all the blocks with the code inside
	print(key, "= {")
	print("\tTAG = {")
	
	for code in value:
		print("\t\t" + code)

	print("\t}\n}")

print("\nCOPY THIS INTO NOTEPAD OR SOMETHING SIMILAR FOR EASE OF USE!")
print("Replace TAG with the tag of the country. NOTE: If the events are from different countries, add another TAG = { block.")
