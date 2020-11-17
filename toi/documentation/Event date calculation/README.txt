Events with a mean time to happen build up and create a not-small amount of lag. A large portion of such events in EoaNB are just events that are supposed to fire near a specific date.
It is way better to, instead, fire it on startup in a specific amount of days. It still allows you to fire around a specific date in a range of days too.
The events are put to trigger in common/on_actions/on_startup_events.txt as to not clutter the other files. 
It is still possible to not make it always trigger by leaving in trigger = {} and just putting is_triggered_only = yes and removing the date check from the trigger.

The scripts are to be opened in Python 3. You can download it in https://www.python.org/downloads/, where you can select any version beginning with 3.

Event_date_calculation.py allows you to easily calculate the amount of days between each start date and the event.
To speed the progress up, just pressing enter without entering a number in the range prompt will assume a range of 100 days.

Reverse_date_calculation.py does the reverse - Given the start date and the amount of days, it allows you to get the end date.
To speed the progress up, just pressing enter without entering the start date will assume the start date of 1857.5.1, the End of a New Beginning bookmark.