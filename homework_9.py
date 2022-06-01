#1

def tuple_check(tuple_1, tuple_2):
	if tuple_1 == tuple_2:
		return True
	if tuple_1 != tuple_2:
	    return False	
				
		    
resulte = tuple_check(tuple_1= (1,2,3,4,5,9,7,0), tuple_2= (1,2,3,4,5,9,7,0))	
print(resulte)




#3



tup_1 = (1,2,3,4,7)
tup_2 =(7, 3,4,5)
new_tuple = list()
def tuple_common_values(tup_1, tup_2):
	for i in tup_1:
		if i in tup_2:
			new_tuple.append(i)
	return tuple(new_tuple)		

final_tiple = tuple_common_values(tup_1, tup_2)	
print(final_tiple)


#4

my_tuple =(7, 3, 3, 4, 5, 7, 1, 9, 1)
new_tuple_1 = list()
def tuple_without_duplicate(my_tuple):
	for i in my_tuple:
		if i not in new_tuple_1:
		    new_tuple_1.append(i)
		
	return tuple(new_tuple_1)	    	

tuple_finish = tuple_without_duplicate(my_tuple)
print(tuple_finish)