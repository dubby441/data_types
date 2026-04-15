# Variable is what contains a value or a container containing a value 
# Value is the content 
# = is called assignment operator 

animal = 'monkey'

book_name = "Don't let him"
pushlished_date = 'Jan 03,2022'
author = 'Jewel'
price = '$20'
color = 'blue'
pushlisher = 'Michael'
pages = 20

# end='' is used to make sure that its on a horizontal line 
#print(book_name,pushlished_date,end='')

#print(type(book_name))

upper = book_name.upper()
#print(upper)

capitalize = book_name.capitalize()
#print("capitalize method", capitalize)

username = "dubby441"
password = "dubby441."
password.lower()
book_name.center

# len is used to count the total numbers of characters 

name = "Hello"
#print(len(name))

#Multiplying a string 
word = "ha"
#print(word*4)

#print(name.spilt(',')) 
#print(name + word) #this is cocantination
#print("-".join(name))

# print("first charater",name[0])

# fullname = name[:4]
# print(name[:])
# print(fullname)

# #[start:end: jump] this is slicing
# # \n means next line  
print(name[::-1])
# print(name[-2])

text = """
today is friday \nand TOMORROW \ni am going to \nvisit a friend.
hello peopel \nhow are you
"""
# print(text)
# print(text.swapcase())

news = "today is good {a} -and tomorrow is {b}".format(a={"easter"},b={"friday"})
# print(news)
