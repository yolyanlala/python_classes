my_text = "this is a string"
print("length of the string" , len(my_text))
# my_text[start:dont_take_this]
print(my_text[0])
print(my_text[-16])
print(my_text[:])
print(my_text[2:6])
print(my_text[-3:-1])
print(my_text[-100:-3])

# my_text[start:dont_take_this:step]
print(my_text[1:100:2])
print(my_text[0:1000:-1])
print(my_text[::-1])
# get is from text

print(my_text[6:4:-1])
text ="Armenia"
print(text.index("Arm"))
print(text.index("nia"))

print(text.endswith("a"))
print(text.endswith("b"))
print(text.endswith(""))
print(text.endswith(" "))

sentence = " Hello python world"
new_one = sentence.replace("python", "django")
print("Old sentence:" , sentence , "New sentence : ", new_one )

sentense_1 = "Hello hello python world"
new_one_1 = sentense_1.replace("ello", "i")
print(new_one_1)

user_name = "john"
age = "28"
part = 0.25

congrats_text = " Dear {} Happy {}-th aniversary you have already lived obout {} part your live"
print(congrats_text.format(user_name, age, part))
print(congrats_text.format("Jack", 38, 0.2))
congrats_text = " Dear {name} Happy {age}-th aniversary you have already lived obout {part} part your live"

print(congrats_text.format(age = age , name = user_name, part = part))
congrats_text_2 = f" Dear {user_name} Happy {age}-th aniversary you have already lived obout {part} part your live"
print(congrats_text_2)

a = "Hello %s" %user_name
print(a)


range_num = range(1, 5, 1)
range_num_1 = range(5)
print(range_num)
print(range_num_1)


print(chr(65))
print(ord("A"))



