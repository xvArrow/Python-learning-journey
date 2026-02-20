first_name= input("Enter 1st student name: ")
first_id= int(input("Enter 1st ID: "))
first_grade= float(input("Enter 1st grade: "))

second_name= input("\nEnter 2st student name: ")
second_id= input("Enter 2st ID: ")
second_grade= float(input("Enter 2st grade: "))
total= first_grade + second_grade
avg= total / 2
first_msg= f"{first_name} (ID {first_id}) got grade: {first_grade}"
second_msg= f"{second_name} (ID {second_id}) got grade: {second_grade}"

print("""\nInformat for students and their "Math" gardes""")
print(first_msg)
print(second_msg)
print("Average math grade is", avg)