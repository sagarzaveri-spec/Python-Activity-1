num1=10
num2=4
# Using AND operator
print("Number 1 & Number 2= ",num1 & num2)
# Using OR operator
print("\nNumber 1 | Number 2= ",num1 | num2)
# Using NOT operator
print("\n~num1= ",~num1)
# Using XOR operator
print("\nnum1 ^ num2= ",num1 ^ num2)

num1=10
num2=4
# Using Right Shift operator on Number 1
print("\nnum>>1=",num1>>1)
# Using Right Shift operator on Number 2
print("\nnum>>1=",num2>>1)

num1=10
num2=4
# Using Left Shift operator on Number 1
print("\nnum<<1=",num1<<1)
# Using Left Shift operator on Number 2
print("\nnum<<1=",num2<<1)

# Odd or even number using Bitwise Operator
def isEvenOdd(n):
    # XOR with 1 equals n+1
    if (n^1==n+1):
        return True
    else:
        return False
    
Number=int(input("Enter the number: "))

if isEvenOdd(Number):
    print(Number,"is Even")
else:
    print(Number,"is Odd")

# Number of Bits
def NumberofBits(n):
    count=0
    while (n):
        count+=1
        n>>=1
    return count
number=int(input("Enter the number: "))
print("Total bits: ",NumberofBits(number))