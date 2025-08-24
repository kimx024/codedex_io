"""
This code is part of Exercise 41: Countdown
This code works in unison with bday_messages.py
"""

# Import the datetime module, introduced in this exercise, and the other Python script
import datetime, bday_messages

today = datetime.date.today()

# Calculate the next birthdays and calculate the difference between today's date in days
my_next_birthday = datetime.date(2100, 1, 1) # This is not my own birthday out of privacy reasons
days_away = my_next_birthday - today

# Print a random birthday message or show the duration until the next birthday
if my_next_birthday == today:
  print(bday_messages.random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')