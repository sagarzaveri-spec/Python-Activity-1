'''
#Function definition
def myself():
    print('I am Python')
def yourself():
    print('I am Java')
#Function call
myself()
'''

#Parameters
def profile(username,password):
    newpass=username+password
    print("New Password: ",newpass)
profile("Sagar","AW#@")

def add(x,y,z):
    sum=x+y+z
    return sum
    print("Hi")
    print(100)
result=add(100,20,40)
print(result)

def add(x,y,z):
    sum=x+y+z
    return sum
def subtraction(x,y,z):
    sub=x-y+z
    return sub
print("1.Addition")
print("2.Subtraction")
choice=int(input("Enter 1 or 2: "))
if choice==1:
    x=int(input("Enter X= "))
    y=int(input("Enter Y= "))
    z=int(input("Enter Z= "))
    result=add(x,y,x)
    print("Sum=",result)
elif choice==2:
    x=int(input("Enter X= "))
    y=int(input("Enter Y= "))
    z=int(input("Enter Z= "))
    result2=subtraction(x,y,z)
    print("Subtraction=",result2)
else:
    print("Invalid Fucntion")

balance=3000
def check():
    print("Balance: ",balance)
def send():
    global balance 
    amount=int(input("Send Amount: "))
    balance=balance-amount
    print("Send!!",amount)
def cash():
    global balance
    amount=int(input("Cashout Amount: "))
    print("Cashout!!",amount)
print("\m1.Check \n2.Send \n3.Cash")
ch=int(input("Choose: "))
if ch==1:
    check()
elif ch==2:
    send()
elif ch==3:
    cash()
else:
    print("Invalid Option")
print("Balance:",balance)

#recursive function
def recure_factorial(n):
    if n==1:
        return n
    else: 
        return n*recure_factorial(n-1)
num=int(input("Enter a number: "))

if num<0:
    print("Sorry, factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",recure_factorial(num))