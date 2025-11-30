'''
#data conversion form integer to float or string to integer
age=int(input('Age: '))
print(type(age))
weight=float(input('Weight: '))
print(type(weight))

name=input('Enter name: ')
age=int(input('Age: '))
weight=float(input('Weight: '))   
student_id=True
print("name: ", name)
print("Age: ",age)
print("Weight: ",weight)
print("Do they have a student ID: ",student_id)
'''

'''
#arithmentic functions
number1=int(input("Number 1: "))
number2=int(input("Number 2: "))

sum=number1+number2
subtraction=number1-number2
multiplicaton=number1*number2
division=number1/number2
floordivision=number1//number2
modulus=number1%number2
square1=number1**2
square2=number2**2
squareroot1=number1**0.5
squareroot2=number2**0.5

print(sum)
print(subtraction)
print(multiplicaton)
print(division)
print(floordivision)
print(modulus)
print(square1)
print(squareroot2)

print("Equal?",number1==number2)
print("Not Equal?",number1!=number2)
print("Number 1 greater than Number 2",number1>number2)
print("Number 1 smaller than or equal to number 2",number1<=number2)
'''

'''
#concatenation
firstname=input("First Name: ")
lastname=input("Last Name: ")
fullname=firstname+" "+lastname
print("Fullname: ",fullname)

#length
text="Codingal"
print(len(text))

#indexing
print(text[3])

#slicing
text2="FIFA WORLD CUP"
print(text2[0:4:1])
print(text2[0:4:2])
print(text2[0:4:3])
#text reverse
print(text2[::-1])


#string matching with indexing
text3="I am eating pizza for dinner"
sub="pizza"
index=text3.find(sub)
print(index)
'''

'''
amount=int(input('Amount: '))
notes_500=amount//500
remaining_amount=amount%500
notes_200=remaining_amount//200
remaining_amount=remaining_amount%200
print("Notes of 500 Rupees: ",notes_500)
print("Notes of 200 Rupees: ",notes_200)
print("Remaining Amount: ",remaining_amount)
'''

#Number Swapping
a=int(input("a: "))
b=int(input("b: "))
a,b=b,a
print("Value of a: ",a)
print("Valye of b: ",b)


a=int(input("a: "))
b=int(input("b: "))
y=a
a=b
b=y
print("Value of a: ",a)
print("Valye of b: ",b)

