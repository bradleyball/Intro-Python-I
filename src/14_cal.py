"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def get_month_and_year():
    month = input("Please select the month:")
    year = input("Please select the year:")
    try:
        if year != "" and month != "":
            year = int(year)
            month = int(month)
        elif year != "":
            year = int(year)
        elif month != "":
            month = int(month)

        if month == "" and year == "":
            return calendar.month(datetime.today().year, datetime.today().month)
        elif month != "" and year == "":
            return calendar.month(datetime.today().year, month)
        else:
            return calendar.month(year, month)
    except:
        print('\033[91m THE PROGRAM EXPECTS MONTH TO BE A NUMBER GIVEN IN THIS FORMAT <MM>\nAND YEAR TO BE A NUMBER GIVEN IN THIS FORMAT <YYYY> \033[0m')


print(get_month_and_year())
