#1
number_of_day = int(input("Enter one of the numbers 0 or 7 and know the day of the week !!\n"))

if number_of_day == 0:
    print("You chose Sunday!")
elif number_of_day == 1:
    print("You chose Monday!")
elif number_of_day == 2:
    print("You chose Tuesday!") 
elif number_of_day == 3:
    print("You chose Wednesday!")     
elif number_of_day == 4:
    print("You chose Turesday!") 
elif number_of_day == 5:
    print("You chose Friday!")    
elif number_of_day == 6:
    print("You chose Saturday!")   
print("Have a good day!!!")  

#2
some_text = input("Write something!  \n ")   
if " " in some_text:
    print( "There is a space")
else:
    print( "There is not a space") 

#3



given_string = input("write some word! \n")
string_length = len(given_string)
if string_length < 3:
    print(given_string)
elif("ing" in given_string):  
    print(given_string +"ly")
else:
    print(given_string + "ing") 


#4
given_year = int(input("Enter the year and check if it is a leap year? \n"))
if given_year % 100 == 0 and given_year % 400 == 0 and given_year % 4 == 0:
    given_year_str = str(given_year)
    print(given_year_str + " is leap year!")

elif  given_year % 100 != 0 and given_year % 4 == 0:
    given_year_str = str(given_year)
    print(given_year_str + " is leap year!")
else:
    given_year_str = str(given_year)

    print(given_year_str + " is not leap year!")   

