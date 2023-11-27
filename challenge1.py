# define a function that returns a string with the hour and minute 
# formatted with leading zeros when given valid input
def time(hour, minute,period):
#if the period is pm and the hour is not midnight add 12 to the hour
    if period == "pm" and hour != 12:
        hour = int(hour) + 12
#if the period is am and the hour is noon the hour will be 0
    elif period == "am" and hour == 12:
        hour = 0
#return the time in 24hr format  
    return(f"{hour: 02d}{minute: 02d}")

result = time(12,42,"am")
print(result)