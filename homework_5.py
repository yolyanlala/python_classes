#1
number = int(input("Write a number! \n"))
if number % 5 == 0 and number % 11 == 0:
	print("Your number divisible by 5 and 11 ")
elif number % 5 == 0:
    print("Your number divisible by 5 but not divisible by 11")	
elif number % 11 == 0:
    print("Your number  divisible by 11") 
else:
    print("Your number not divisible by 5 and by 11")      

#2
for num in range(31):
	if num % 3 == 0 and num % 5 == 0:
		print("FizzBuzz")
	elif num % 3 == 0:
	    print("Fizz")
	elif num % 5 == 0:
	    print("Buzz")
	else:
	    print(num) 

#3
sentence = input("Write some sentence ! \n")
#print(sentence)
good = "good"
if "not" in sentence and "poor" in sentence and sentence.index("not") < sentence.index("poor"):
	not_index = sentence.index("not")
	poor_index = sentence.index("poor")
	#print(not_index)
	#print(poor_index)
	new_sentence = sentence[0:not_index] + good + sentence[poor_index + 4:]
	print(new_sentence)

else:
    print(sentence)	
    
	 	
	

   	    



#4
string = input("write something! \n")
first_char = string[0]
#print(first_char)
new_string = string[1:]
#print(new_string)
finish_string = first_char + new_string.replace(first_char,"$")
print(finish_string)

