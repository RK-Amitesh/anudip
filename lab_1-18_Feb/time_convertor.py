#program to input time in seconds & convert it into hours, minutes & seconds
#input of time in seconds
second = int(input("Enter time in seconds: "))
#---------------------------------------------
#initializing no. of hours & minutes
minutes = 0
hours = 0
#calculating hours
if(second >= 3600):
    hours = second // 3600 #storing quotient as hours
    second = second % 3600 #storing remainder as seconds
#calculating minutes
if(second >= 60):
    minutes = second // 60 #storing quotient as minutes
    second = second % 60 #storing remainder as seconds
#printing time in hours, minutes & seconds
print("Time in hours: ",hours)
print("Time in minutes: ",minutes)
print("Time in seconds: ",second)