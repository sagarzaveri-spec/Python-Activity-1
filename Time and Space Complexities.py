'''
#Time Complexity Big O(n)
def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
print(fun2(4))

#Time Complexity Big O(n^2)
def fun3(n)
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum+=1
    return sum
print(fun3(4))
'''

def linear_search(array,key):
    for i in range(len(array)):
        if array[i]==key:
            return i
    return-1
array=[22,44,1,5,7,89]
k=5
result=linear_search(array,k)

if result!=-1:
    print("Data found at index: ",result)
else:
    print("Data not found")