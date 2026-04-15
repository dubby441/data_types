"""
define variable and assign a string value to it.
get the last 3 letters, get first 3 alphabets.
combine them, transform it to capital letters  and reverese afterwards and 
print it out without the last element.

"""
#hospital management 
# hospital = "Nuel hospital"

# bed = "20 beds"

# doctors = "10 doctors"

# p = hospital.replace('Nuel','Dubem')
# print(p)
# print(hospital.split())


club_name = "real madrid"
last_3 = club_name[-3:]
first_3 = club_name[:3]

combine_both = last_3 + first_3
upper_case = combine_both.upper()
reversed_word = club_name[::-1]
without_last_letter = club_name[0:-1]
#print("first 2 letters:",club_name[:2])
print(without_last_letter)

first_4 = club_name[0:4]
#print(len(first_4))
print(reversed_word)