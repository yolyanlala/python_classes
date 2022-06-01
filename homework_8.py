#1

def tryangle_area(ground, height):
	area = ground * height**2
	return area

tryangle_area(4,6)	


print(tryangle_area(4,5))

#2
str_ = "0123456789"
def string_revers(str_):
	len_ = len(str_)
	for i in str_:
		a = str_[::-len_]
		len_ -= 1
				
	return a	
	
string_revers(str_)

new_string = string_revers(str_)
print(new_string)


#3

my_string = input("Write your text!!")

def upper_or_lower(my_string):
	count_upper = 0
	count_lower = 0
	for i in my_string:	
		if i.isupper():
			count_upper += 1
		else:
		    count_lower += 1
	

	text = " Your text have {} upper and {} lower letters ".format(count_upper,count_lower)
	return text   
	
	

upper_or_lower(my_string)
new_text = upper_or_lower(my_string)
print(new_text)



#5

number = int(input("Write a number and check the number is prime or not !\n "))
def num_prime_or_not(number):
	if number == 2:
		print("2 is a prime number!")

	for i in range(2, int(number/2) + 1):
		if (number % i) == 0:
			print(number, "is not a prime number")
			break
	else:
		print(number, "is  a prime number")
		    
	
	


num_prime_or_not(number)
   











