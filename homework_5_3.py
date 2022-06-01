#3
sentence = input("Write some sentence ! \n")
#print(sentence)
good = "good"
if "not" in sentence and "poor" in sentence and sentence.index("not") < sentence.index("poor"):
	not_index = sentence.index("not")
	poor_index = sentence.index("poor")
	#print(not_index)
	#print(poor_index)
	new_sentence = sentence[0:not_index] + good + sentence[poor_index + 4:]
	print(new_sentence)

else:
    print(sentence)	
    
	 	
	

