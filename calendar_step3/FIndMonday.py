
def MySchedule():

	  a="""Day           Time                  Subject
Monday      10:00 - 11:00 AM         Period 1
            11:30-12:30 AM.          Math
Tuesday     9:00-11:00 AM            PE
            10:00-11:00 AM.          Science"""
	  return a



calendar=MySchedule()

#This is to check if the word "Monday" is present in my code
if "Monday" in calendar:
	print("Monday is present")
else:
   	print("Monday is not in the schedule")

#This is to print the code in upper case
print(calendar.upper())