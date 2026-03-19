# One Odd Occurring Number
def one_odd(arr):
    result=0
    i=0
    while i<len(arr):
        result^=arr[i] #XOR operation
        i+=1
    return result
arr=[2,3,2,3,4]
print("Odd occuring numbers: ",one_odd(arr))

# Two Odd Occurring NumberAlgorithm
# 1. XOR all elements
# 2. Find the right-most set bit -- XOR & (-XOR)
# 3. Divide into two groups
   # g1 --- bit is set
   # g2 --- bit is not set
# 4. XOR each group

def two_odd(arr):
    XOR=0
    i=0
    # Step 1: XOR all elements
    while i<len(arr):
        XOR^=arr[1]
        i+=1
    # Step 2: Find the right-most step bit
    set_bit=XOR&(-XOR)
    x=0
    y=0
    i=0
    # Step 3 & Step 4
    while i<len(arr):
        if arr[i]&set_bit:
            x^=arr[i]
        else:
            y^=arr[1]
    return x,y
arr=[4,2,1,2,4,1,4,2,1]
a,b=two_odd(arr)
print("The odd occurring numbers: ",a," ",b)

# Check if two numbers are equal without using the comparitive operator
def checkifsame(number1,number2):
    if((number1^number2)!=0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")
number1=int(input("Enter the first number to compare: "))
number2=int(input("Enter the second number to compare: "))
checkifsame(number1,number2)