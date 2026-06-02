students = ['Mary', 'James', 'John', 'Peter', 'Paul','Jack']
highest = 100

score = int(input("Enter a student's score: "))
if score == highest:
    student_name = students[1]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'Excellence'}")

elif score >= 75:
    student_name = students[0]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'A'}")

elif score >= 65:
    student_name = students[4]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'B'}")

elif score >= 50:
    student_name = students[5]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'C'}")

elif score >= 35:
    student_name = students[2]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'D'}")

elif score >= 0 or score < 35:
    student_name = students[3]
    print(f"Student Name: {student_name}\nscore: {score}\nGrade: {'F'}")

else: 
    print(f"Invalid result")

   