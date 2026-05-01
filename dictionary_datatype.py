my_dict = {'name':'Nuel', 'surname':'Edward', 'age':31, 'phone no':(690809890890,90049498940)}
print(type(my_dict))
print(my_dict)

friends = {'john':'08099944897', 'Mike':957484774774, 'Mary':8474737373874784}
print(friends)

name = my_dict['name']
print(name)
key_items = my_dict.keys() # to print only the keys in a dictionary
print(key_items)
values = my_dict.values() # to print only the values and leave the keys in a dictionary
print(values)
items = my_dict.items() # to print the keys and values in pairs 
print(items)

age = my_dict['age']  
print(age)
my_dict['name'] = 'Chidubem'# this is to update a value in a key
print(my_dict)

my_dict['height'] = 5.7 #to update a value however is there is no key with that name it will add the key and value
print(my_dict)

address = my_dict.get('address','no valid address')
print(address)

print(len(my_dict))

dict_function = dict(name = 'James', phone_no =893838293, country = 'Nigeria')
print(type(dict_function))
print(dict_function)

print('name' in my_dict) #to check if name is my_dict
#del my_dict #deletes the whole variable 

phones = {'samsung':'$2000','Iphone':'$3400','redmi':'$1500'}
print(phones)
print(phones.keys())
key_list = list(phones.keys()) # this is type casting/converting the dict to list to print only the keys
print(key_list)
key_values = list(phones.values()) # this is type casting/converting the dict to list to print only the values
print(key_values)

items1 = list(phones.items()) # this is type casting/converting the dict to list to print the items one at a time 
print(items1)

#nested dictionary which is a dictionary inside a dictionary

university = {
    'English Language':{
        'teacher':'Nuel',
        'student':30,
        'time':'9:30am',
        'phone no':[90990008808,837362773737]},
    'Programming':{
        'teacher':'Dubem',
        'students':45,
        'time':'10:30am',
        'phone no':646474764},
    'Maths':{
        'teacher':'Mrs Mary',
        'students':50,
        'time':'12:00pm',
        'phone no':4554343334}
}
print(university)
print('teacher' in university)
print('English Language' in university)
print('teacher' in university['English Language'])

#two ways of using dictionary 
d = {'laptop':'mac pro 16'}
e = dict(laptop = 'mac pro 16')

fruits = ['banana','oranges','grapes','apples']
fruit_items = dict.fromkeys(fruits,50) # to assign 50 to all the list values using dict function
print(fruit_items)

d.update(fruit_items) # adding the fruit_items to the d variable 
print(d)

d.update({'cashew':30,'mango':40,'strawberry':80}) #another way to use update 
print(d)

copy = d.copy()
print(copy)
#d.clear() #this is to clear everything in the d variable 

d.pop('cashew') #this is remove only cashew
print(d)

d.popitem() #this will remove the last item if no value is added
print(d)

No_students = university['Programming']['students'] #trying to get the number of students in programming class that is inside university
print(No_students)

