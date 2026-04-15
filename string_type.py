#to add - to the string 
full_name = "chidubem okpala"
print("-".join(full_name))

name = "-".join(full_name)
print(name)

#checking the length of string
print(len(full_name))

#to add space to the string 
print(full_name.rjust(20,"-"))
print(full_name.ljust(20,"*"))

#this is add a partition in a string which seperates into three
print(full_name.partition(" "))
#print(full_name.partition(","))
print(full_name.split(" ")) # split seperates into two 

first_name = "OKPALA"
print(first_name.swapcase()) #to change the character of a string

text = """hello dubem how are you today?
will you like to come for a visit today?
tell me the time convenient for you.
hope to see you later."""

#\n is used to start a new line
word = "today is a good day\n to start learning python. I hope you learn and understand very well."
print(word)

# formatting 
username = "harry"
password = "okpala"

user_info = f"my username is {username} and my password is {password}"
print(user_info)

user_details = "my name is {a} and I am a software {b} and AI {c}".format(a="Chidubem Okpala", b="Engineer", c="Professional")
print(user_details)

#slicing 
greating = "hello world"
print(len(greating))
first = greating[0]
print(greating[0:5])
print(greating[0:8:2])
print(greating[1:-1])

email,phone_no = "dubby@gmail.com","0994474747"
print(email)
print(phone_no)

number = "45"
print(number.zfill(7))