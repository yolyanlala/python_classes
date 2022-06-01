#1 
set1 = {"Yerevan", "Goris", "Gyumri"}
set_copy = set1.copy()
print (set1)
print (set_copy)
set1.add("Ararat")
print (set1)
print(set_copy)



#2
my_set = {7, 4, 8, 45, 33, 68, 547, 22}
max_ = max(my_set)
min_ = min(my_set)
print(f"MAX element in my set is {max_} and MIN  element in my set is {min_}" )

#3
set_1 = {2, 5, 7, 34, "hello", " hay", "Armenia", False, 8888}
set_2 = {3 , 7, False , "hello" ,"Armenia", 90, 56}
finish_set = set()
for item in set_1:
	if item not in set_2:
		finish_set.add(item)

print(finish_set)


