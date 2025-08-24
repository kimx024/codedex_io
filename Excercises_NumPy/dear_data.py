"""
Python: NumPy
This code is part of Exercise 6: Dear Data
This exercise wraps up the last exercise of the Chapter and is the last exercise of the first chapter about NumPy.


In this final exercise, you are going to capture some data from your day-to-day... using NumPy arrays! 🔢
Think of something that you do within a day or within a week that can be observed with some number.

Some inspirations could be:
🍵 Recording your mood (out of 10) in each waking hour today.
💤 How many hours you slept.
💧 The number of glasses of water you drink every day this week.
🥱 The number of yawns.
👀 How many ____ you ____.
Use your phone's notes or a notebook to capture this data and then store them in an array.

Does this make sense to keep this data in a 1D array or a 2D array?

Now, use index and slicing to analyze it a bit - what is the average number during waking hours?
How about what is the difference between the beginning and the end of the duration?
"""

import numpy as np

# First topic of choice: how many hours I approximately slept last week. 💤
weekly_sleep_hrs = np.array([6.4, 7.3, 8.2, 5.0, 7.8, 8.5, 8])

# Second topic of choice (extra): how many hours I approximately slept last month. 💤💤
monthly_sleep_hrs = np.array([[7.0, 7.3, 8.0, 6.5, 6.5, 8.0, 8.2],
                             [6, 5, 7.5, 6.6, 8.2, 8.0, 8.5],
                             [7.6, 6.5, 8.3, 7.7, 8.4, 8.0, 8.4],
                             [6.4, 7.3, 8.2, 5.0, 7.8, 8.5, 8]])

"""
=== Explanation===
For something that doesn't need a lot of depth or where the sequence is more important, a 1D array
suffices. For something more detailed or focused on the individual entries, a 2D array is more important.
Hence, why weekly_sleep_hrs is a 1D array and monthly_sleep_hrs is a 2D array
"""

# Modifications with slicing and calculations
weekly_workweek = weekly_sleep_hrs[0:5]
monthly_workweek = monthly_sleep_hrs[:, :5]
print(f'Weekly (Mon–Fri): {weekly_workweek} \n'
      f'Monthly (Mon–Fri for each week: {monthly_workweek} \n')


average_workweek_weekly_hrs = np.average(weekly_workweek)
average_workweek_monthly_hrs = np.average(monthly_workweek)
print(f'Average of last week: {average_workweek_weekly_hrs} \n'
      f'Average of last month: {average_workweek_monthly_hrs} \n')

# Conclusion
print("Conclusion: The average sleep hours of last week is under the average of the month")

