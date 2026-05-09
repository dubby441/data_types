# set is a collective data type and it is unordered and can be mutible and unmutible and does not accept duplicate 
# an argument is a value you paas in a function
myset = set()
my_set1 = {'mango','apple','orange','cashew','mango','orange',4,5,7,}
print(my_set1)

my_set1.add('jerry') # this takes one argument at a time 
my_set1.update(['king','Queen']) # this method adds more than one argument
print(my_set1)

leaders = {'Trump','Buhari','obi','Dubem'}
my_set1.update(leaders) #adding two sets 
print(my_set1)

personal_properties = {'car','bike','phone'}
tv_sets = {'LG','Samsung','Sony','Hp'}

belongings = personal_properties | tv_sets #another way of adding two sets together
print(belongings)
belongings.discard('Hp')
print(belongings)

belongings.pop() # this will remove a value randomly
print(belongings)
# belongings.clear() #this clears the whole set 

bel = belongings.copy
print(bel)

items = {'pen','pencil','ruler','chalk','python'}
course = {'python','java','javascript','.Net','pen'}

studies = items.union(course) #union create a new set while update adds to the existing values
print(studies)

common_values = items & course #this is called intersection
print(common_values)
common = items.intersection(course)# another method of using intersection
print(common)

diff = items - course #this shows the things that they do not have in common
print(diff)
diff2 = items.difference(course) #another method to using difference
print(diff2)

#to get a range of numbers 
print(set(range(1,11)))
#range(start:stop:step)
print(set(range(1,11,2)))

set_values = {3, True,2,6,3,False,0}
print(set_values)

