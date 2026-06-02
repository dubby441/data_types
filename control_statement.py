# presenter = 'Nuel' 
# name = input('Enter your name:')

# if name == presenter:
#     print(f"{name} is currently presenting")

# else:
#     print("Incorrect presenter")

# #checking if password holds any value 
# password = "12345"
# if password:
#     print("correct")
    
# else:
#     print("Nothing")
    
# num1 = 20
# num2 = 30

# if num1 != num2:
#     print("they are not the same value")
    
# else:
#     print("they have the same value")            

# voting_age = 18
# voter_name = input("Enter your name:")
# age = int(input("Enter your age:"))

# if age >=18:
#     print(f"{voter_name}, please proceed to vote")
    
# else:
#     print("You are not eligible to vote")    


# teacher = input("Enter your name:")
# if teacher == "Nuel":
#     print(f"Hello, {teacher} you are taking python programming students")

# elif teacher == "John":
#     print(f"Hello, {teacher} you are taking English students")

# elif teacher == "Jerry":
#     print(f"Hello, {teacher} you are taking Maths students")
 
# elif teacher == "Mary":
#     print(f"Hello, {teacher} you are taking History students")

# elif teacher == "Jack":
#     print(f"Hello, {teacher} you are taking Javascript students")

# else:
#     print(f"Hello, {teacher} you are not recognized yet. Contact the admin")


# username = "dubem123"
# password = "dubby1"

# user_input = input("enter your username: ")
# user_password = input("enter your password: ")

# if not user_input:
#     print("Your username must not be empty!")
# elif user_input == username and user_password == password:
#     print(f"Welcome, {user_input}")

# else:
#     print("Everything is not correct.")

number = int(input("enter a numebr: "))
if number % 2 == 0:
    print("even number")
else:
    print("odd number")

num1 = 2
num2 = 20
if num1 > num2:
    print (f"{num1} is bigger than {num2}")

bigger_value = num1 if num1 > num2 else num2
print(f"{bigger_value} is bigger")