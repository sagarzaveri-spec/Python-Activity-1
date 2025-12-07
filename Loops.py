'''
name="Sagar"
for i in name: 
    print(i)
for j in range(5):
    print("For Loop range")
    print(j+1)
'''

'''
#series sum
sum=0
for k in range(1,51):
    sum=sum+k
print(sum)
'''

'''
#sum of 2+4+6+8...n
sum=0
lower=2
upper=100
for l in range(2,101,2):
    sum=sum+l
print(sum)
'''

'''
#Nested for loops
adjective=["red","healthy","tasty"]
fruits=["apple","banana","cherry"]
for x in adjective:
    for y in fruits:
        print(x,y)
'''

'''
#table of 23
for i in range(2,101,4):
    print(f"21x{i}={23*i}")
'''

'''
#patterns
n=int(input("Row: "))
for row in range(n,0,-1):
    for column in range(row):
        print("*",end=" ")
    print()
'''

number=int(input("Number to be checked: "))
flag=False
if number>1:
    for i in range(2,number):
        if(number%2)==0:
            flag=True
            break
if flag==True:
    print(number,"is not a primen number")
else:
    print(number,"is a prime number")