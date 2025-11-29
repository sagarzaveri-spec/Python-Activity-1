'''
print("Enter number1:")
x=int(input("Number1="))
y=int(input("Number2="))
z=x+y
print(z)
'''
#string data type
student_name='Sagar'
#integer data type
age=20
college_name='JHC'
#decimals are called as floating point. 
#floating point data type
cgpa=9.92
print(student_name)
print("Student Name= ",student_name)
print("Student Age: ",age,"College name: ", college_name)
print(f"My name is {student_name}.I study in {college_name} college.")

#function definition
def welcome(name,message):
    print(f"{name} welcome to this world {message}")
#function call
welcome("Sagar","Congratulation!")

#Conditional Statement
n=int(input('Enter to check Odd or Even: '))
if n%2==0:
    print("Even")
else:
    print("Odd")

    