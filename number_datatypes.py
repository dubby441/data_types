# a whole number is known as integer
# a number with decimal is called float 
# complex number have alphabet(j) which is called an imaginary alphabet attached to it mainly for machine learning
# = is called assignment operator

num1 = 20
num2 = 20.4554

num3 = num1 + num2
print(num3)

num4 = 2 + 3j
num5 = 4 + 5j
print(num4 + num5) #addition

num_1, num_2 = 5, 10
num_2 - num_1 #subtraction

num_one = 7
num_two = 2
print(num_one / num_two) #Divison operator
print(type(num1))
print(type(num2))
print(type(num4))

num_one * num_two # multiplication operator 

aws = num_one // num_two #floor operator removes reminder
print(aws)

aws1 = num_one % num_two # modulus operator prints only the reminder
print(aws1)

min = -5 
abs(min) #abs means absolute number changes negative number to postive
print(abs(min))

pw = 2 ** 8 # exponent - multiply to the power 
print(pw)

new_num = 3.454
rd = round(new_num, 1) #rounding up demical numbers
num = [3,5,6,7] #list
print(max(4,6,8,9))

import math 

n1 = 4.85
ceil = math.ceil(n1) # takes it up to the nearest whole number
print(ceil)
flr = math.floor(n1) # takes it down to the nearest whole number
print(flr)

import random 
rnd = random.random() #prints randon float numbers not get up to 1
print(rnd)
ten = random.randint(1,10) # prints random integer
print(ten)

students = ['nuel','joy','mike','esther', 'john']
name = random.choice(students) # picks one random name from the list
print(name)
print(random.sample(students,3)) #picks 3 random names from the list