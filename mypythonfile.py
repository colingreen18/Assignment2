"""
mypythonfile.py

A program that greets you with the date
"""
from datetime import date
today = date.today()
monthDayYear = today.strftime("%B %d, %Y")

user = input("Please enter your name: ")
print(user)
print("Hello " + user)
print("Today is %s" % monthDayYear)
