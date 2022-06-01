#1

km = int(input("Tell the kilomert and see the mile :\n " ))
mile = km / 1.609344
print( km , " kilomert is " ,  mile , "mile")

#2



import rate
print(rate.rate_1_usd)
amd = int(input("Tell me how amd you have and see how usd is it : \n" ))

usd = amd / rate.rate_1_usd
print("You have ", usd , "UDS")

#3
print("Do you want to now your optimal weight?")
weight = int(input(" Write your height and see your optimal weight :\n "))
optimal_height = (weight - 110) * 1.15
print("Your optimal height is " , optimal_height)

#4
print("Welcome our Foodcourt!")

order = int(input("If you whant Pizza write 1, If you whant qyabab write 2 ! \n "))

print(order)
addition = int(input("for ketchup write 3, for mayonez 4 \n" ))
print(addition)

finish_order = str(order)+ str(addition )
end_finish_order = int(finish_order)


print(bool(end_finish_order % 13 == 0) * "You have ordered pizza with ketchup and your price is 1100  ")
print(bool(end_finish_order % 14 == 0) * "You have ordered pizza with Mayonez and your price is 1500  ")
print(bool(end_finish_order % 23 == 0) * "You have ordered qyabab with ketchup and your price is 900 ")
print(bool(end_finish_order % 24 == 0) * "You have ordered qyabab with Mayonez and your price is 1300 ")

