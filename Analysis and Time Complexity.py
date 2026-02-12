'''
T(n)=T(n/2)+O(1)
Step 2:
T(n)=T(n/2)+c
T(n/2)=T(n/4)+c
T(n)=T(n/4)+2c
……
It will stop until we get n/2^k=1
k=logn
T(n)=clogn
Time complexity O(logn)
'''

'''
def fun(n):
    if n<=1:
        return
    fun(n-1)
    fun(n-1)
'''

'''
Merge sort algorithm
1. Divide array in two halves
2. Recursively sort both halves
3. Merge the two sorted halves

Example: [8,1,3,5,2,9,]
1. Divide [8,1,3] and [5,2,9]
2. Then combine
'''

def merge_sort(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=merge_sort(array[:mid])
    right=merge_sort(array[mid:])
    return merge(left,right)

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

array=[98,3,5,2,9,1]
print(merge_sort(array))