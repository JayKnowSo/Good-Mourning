# Notes: Practicing user input
# Using if/ elif/ else for decision making
# Variables store user responses
# f-strings format output messages
import datetime
# get current hour
current_hour = datetime.datetime.now().hour

# decide time of day
if current_hour < 12:
    time_of_day = "Mourning"
elif current_hour < 18:
    time_of_day = "Afternoon"
else: 
    time_of_day = "Evening"
 # ask user for name
name = input("enter your name:") # the person we want to greet
print(f"Good {time_of_day}, {name}!")