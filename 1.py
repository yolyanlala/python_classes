# # a = ("a", "and", 1, False, "aaa" )
# # b = ("hhh", "5", True, 768, "aoou")

# # def check_string_amount(a, b):
# # 	type_of_strings = (str)
# # 	amount_a = 0
# # 	amount_b = 0
# # 	for i in a:
# # 		if type(i) in type_of_strings:
# # 			amount_a += 1
# # 	for j in b:
# # 	    if type(j) in type_of_strings:
# # 	        amount_b += 1		
	
# # 	if amount_a == amount_b:
# # 		return True 


# # check_string_amount(a, b)

# def sum_letters(tuple_1: tuple) -> int:
# 	count_ = 0
# 	for item in tuple_1:
# 		if type(item) is str:
# 			for let in item:
# 				if let.isalpha():
# 					count_ +=1
# 	return count_
	
# def compare_letters_count_for_tupels(tup_1, tup_2):
#     return sum_letters(tup_1) == sum_letters(tup_2)

# def compare_letters_count_for_multiple_tupels(*args):
# 	chack = False
# 	first_count = sum_letters(args[0])
# 	for tuple_ in args[1:]:
# 		if sum_letters(tuple_1)!= first_count:
# 			return chack

# 	return True

# t_1 =("abc" , 56, "j8k")
# t_2 = ("gh" , 56 , "ko")


# print(compare_letters_count_for_tupels(t_1, t_2))
# # print(compare_letters_count_for_multiple_tupels(t_1, t_2))

a = (1,2)
list_1 = list(a)
list_2 = list(a)
list_3 = []

list_1.append(True)
list_1.append([1,2])
list_1.append((5, False))


print(list_1,id(list_1))
list_1.insert(0, "text")
print(list_1, id(list_1))

list_1 = list_1 + list_2
print(list_1)

print("removing")
list_1.remove("text")
list_2 = list_1.pop()
del list_1[0]
list_1 

my_list =[2,4,7,9,2,30]
def second_larged_value(list_):
	list_2 = my_list.copy() 
	list_2.sort()
    return list_2[-2]
a = second_larged_value(my_list) 
print(a)













