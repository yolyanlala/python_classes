#1

num = int(input("Tell a number ! \n "))
if num == 0:
	print("The factorial of 0 is 1")
if num < 0:
    print("Negativ number does not have a factorial") 
else:
    factorial = 1

    for i in range(1, num +1):
	    factorial = i*factorial
    print(f" The factorial of {num} is {factorial} !")

#2



for x in range(6):
	print(x * "*")
y = x-1	
a = 0
while y > a:
    print(y * "*")
    y -= 1 	    


#3 


a = 0
b = 1
while a + b < 51:
	c = a + b
	print(c)
	a = b
	b = c



#4



import random
user_action = int(input("Choice: 1 is rock, 2 is paper ,3 is scissors \n"))

computer_action = random.randint(1,3)
print(computer_action)

if user_action == computer_action:
	print(" It's a tie! Try again.")
elif user_action == 1:
	if computer_action == 2:
		print("Paper covers rock! You lose.")
	elif computer_action == 3:
		print("Rock smashes scissors! You win!")
elif user_action == 2:
	if computer_action == 1:
		print("Paper covers rock!You win!")
	elif computer_action == 3:
	    print("Scissors cuts paper! You lose")
elif user_action == 3:
    if computer_action == 1:
        print("Rock smashes scissors! You lose")	
    elif computer_action == 2:
        print("Scissors cuts paper! You win !") 
print("GAME OWER!!!")       	

	
