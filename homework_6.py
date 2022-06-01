#1
for x in range(10):
	print(x * "*")


#2

count_even = 0 
num = "25252525252525"
for i in num:
	if i.isdigit() and int(i) % 2 == 0:
	    count_even += 1
print(count_even)		    



#3
a = 1
for b in range(2, 10):
	print("{} x {} = {}".format(a, b , a*b))
	a = a + 1


#4
string = "H_e_l_l_o   W_o_r_l_d_!"
new_string = string[::2]
print(new_string)

for i in range(0, len(string), 2):
	print(string[i])



#5
number = int(input("Write a number and know the divisors of that number.\n"))
for i in range(1, number + 1 ):
	if number % i == 0:
		print("{} is divisors of ".format(i), number)
	
