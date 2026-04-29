# a tuple is an ordered and immutible(you can not change the value) while list is mutible  
# tuple is faster than list 
# tuple has smaller memory size than list 

myvalue = (30,58,49,[9,8,3],(4,3,2),7,3)
print(type(myvalue))

first = myvalue[0]
print(first)

second = myvalue[3][1]
print(second)

my_numbers = 20,30,50
print(my_numbers)
print(type(my_numbers))

first_3 = myvalue[:3]
print(first_3)

print(myvalue.count(7)) #tells you how many times 7 appears
print(myvalue.index(7)) #tells you which position is 7 counting from 0

my_t = (4,5,6,7,8,9)
print(my_t[::-1]) #print the values from the last to the first

colors = ('green','white','blue','black','yellow')
*all_colors,one_color = colors #this takes everything in colors and assign it to the first variable leaving the last value to the second variable 
print(all_colors)
print(one_color)
first_3 = colors[:3]
last_2 = colors[-2:]
print(first_3)
print(last_2)

      
      
