first = "Nuel" , "Edward" #this is turple because a string value or a data type holds one value at a time
print(first)
print(type(first))

#list is a collective data types that holds more than one value at a time

friends = ['peter','Mary','James','Nuel']

first_item = friends[0]
print(first_item)

list_items = friends[:3]
print(list_items)
last = friends[-1]
print(last)

length = len(friends)
print(length)

last_2 = friends[-2:] 
print(last_2)

friends.append('Paul') #append adds more values to the list
print(friends)

friends.insert(0,'Dubem') #insert specifies the postion where you want to place the value 
print(friends)

number_set = [2,4,5] *3
print(number_set)

steps = friends[::2] #this is to skip one value each
print(steps)

friends[1] = 'Harrison' #replace a paticular value by placing the postion of that value 
print(friends)

friends[1:3] = ['mango','cashew'] #to replace more than one value in a list
print(friends)

phones = ['iphone','samsung','redme']
laptop = ['mac','hp','dell']
print(phones + laptop) #this is called concantination

print(len(friends))
friends.pop() #this removes  the last value of the list called first in last out
print(len(friends))

friends.remove('mango') #this helps to remove a specific value in a list mentioned
print(friends)

friends.pop(1) #this removes the position of value 
#print(friends)

del friends[1]
print(friends)
#del friends deletes the variable completely 

#friends.clear() #removes the whole value in a variable 
#print(len(friends))

print('Dubem' in friends) #this is to check an item in a list
print(friends)
print(friends.index('Nuel')) #this checks the position of an item
count = friends.count('Dubem') #counts how many times an item appears
friends.append('harry')
print(friends)

nums = [3,1,0,4,2,30,9]
nums.sort() #this hleps to arrange numbers from the lowest to the highest
print(nums)
nums.sort(reverse=True) #arranges the numbers from the biggest to the smallest
print(nums)

phones.sort()
print(phones)

phones.sort(reverse=True)
print(phones)

family = ['tina','john','ada']
family_2 = sorted(family) #the difference between this sorted snd sort is that you can assign this to a variable but sort can not 
print(family_2)
family.reverse()
print(family)

nums = [3,1,0,4,2,30,9]
total = sum(nums)
print(total)

mx = max(nums)
print(mx)
mn = min(nums)
print(mn)

avg = total / len(nums)
print(avg)

rg = list(range(10))
print(rg)

first, second, third = ['tina','john','ada']
print(first)
print(second)

jn = " ".join(family)
print(jn)

first, *rest = [20,50,40,10] # the * take the the remaining values after first to rest
print(first)
print(rest)
*mylist,last = [44,20,19,28,43] # the * takes all the values and assign it to mylist and leaves the last value to last 
print(mylist)
print(last)
