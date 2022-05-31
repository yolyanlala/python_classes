import datetime
current_date = datetime.datetime.now()
year = current_date.year
print(year)
year_= str(year)

sum_ = 0
for i in year_:
	print(i)
	sum_ += int(i)

print(sum_)



text = "a1a1"

count_num = 0
count_let = 0
for num_ in text:
	if num_.isdigit():
	    count_num += 1
	elif num_.isalpha():
	    count_let +=1   
print(count_num)	
print(count_let)

count_num1 = 0

for i in text:
	if i.isdigit():
		count_num1 +=1
	else:
	    print("couldnt fine")
	    #continue
	    break
	print("Ive founde one more number")    	


sum_= 0

for nun_2 in range(1,21):
	if nun_2 == 3 and nun_2 == 13:
		continue
	
	sum_ += nun_2	






