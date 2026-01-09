import datetime
# get current hour
current_hour = datetime.datetime.now().hour

#decide time of day
if current_hour < 12:
    time_of_day = "mourning"
elif current_hour < 18:
    time_of_day = "afternoon"
else: 
    time_of_day = "evening"

 # ask user for name
name = input("enter your name:")    # the person we want to greet
print(f"good {time_of_day}, {name}!")