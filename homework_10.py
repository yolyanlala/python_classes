#1
def between_elementsin_in_list(list_1, list_2):
    my_list = []
    for item in list_1:
        if item in list_2 and item not in my_list:
            my_list.append(item)
    return my_list          
    
l_1 = [1,1,3,4,5,6,7, 'iii', True] 
l_2 = [1,3,'iii', 6,2,True,9]  
finish_list = between_elementsin_in_list(l_1, l_2)    
print(finish_list)

#2

sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]   
       
def remove_dublicates_from_a_list(list_:list ):
    new_list = []
    for item in list_:
        if item not in  new_list:
            new_list.append(item)
    return new_list
new_my_list = remove_dublicates_from_a_list(sample_list) 
print(new_my_list)           
  
 #4
string_ = input("Write something and i will  print it back with the words in backwards order \n")
def print_backwards_order(some_string):
    
    text_list = some_string.split()
#print(text_list)
    text_list.reverse()
    return text_list

finally_text =print_backwards_order(string_)   
print(*finally_text)  
    
            
#3
def my_function(my_list:list):
    new_nested_list = []
    for i in my_list:
        if type(i) is int:
            new_nested_list.append(i)
    for k in my_list:    
        if type(k) is list:
            for j in k:
                new_nested_list.append(j)  
            
            
    return new_nested_list

b = [2, 3, [20, 30], 20, [60, 70, 80], [90, 100, 110, 120],]    
new_ = my_function(b)    
print(new_)
