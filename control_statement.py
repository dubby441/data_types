presenter = 'Nuel' 
name = input('Enter your name:')

if name == presenter:
    print(f"{name} is currently presenting")

else:
    print("Incorrect presenter")

#checking if password holds any value 
password = "12345"
if password:
    print("correct")
    
else:
    print("Nothing")
    
num1 = 20
num2 = 30

if num1 != num2:
    print("they are not the same value")
    
else:
    print("they have the same value")            

voting_age = 18
voter_name = input("Enter your name:")
age = int(input("Enter your age:"))

if age >=18:
    print(f"{voter_name}, please proceed to vote")
    
else:
    print("You are not eligible to vote")    