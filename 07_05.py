#radius = float(input("Tell a radius \n "))

#area = 3.14 * radius**2
#print(area)


#name = input("name\n")
#surname = input("surname\n")

#print( surname, name)

#import variables
#print("current date is : ", variables.year , variables.month, variables.day)
import variables as vbs

print("current date is:", vbs.year, vbs.month, vbs.day)


import datetime
current_date = datetime.datetime.now()
print(current_date)
print(current_date.date())
print(current_date.time())
print(current_date.year)
print(current_date.month)
print(current_date.day)

age = int(input("Tell your age\n"))

_year = current_date.year - age + 100
print("You will be 100 years old in", _year)

