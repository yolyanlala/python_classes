
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={6:50,7:60}
new_dict = {}
for a in (dict1, dict2, dict3, dict4):
	new_dict.update(a)
print(new_dict)



#2
my_dict = {}
for n in range(1,6):
	my_dict[n] = n*n
print(my_dict)

# 3 

dict1 = {"c1": "Red", "c4": None, "c2": "Green", "c3": None, }
def drop_non_from_dict(dict_):
	for item, value  in dict(dict_).items():
		if value is  None:
			del dict_[item]
	return(dict_)

finish_dict = drop_non_from_dict(dict1)
print(finish_dict)

