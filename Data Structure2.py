my_tuple=('Python','Java','C#')
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])
for i in my_tuple:
    print(i)

print(my_tuple[:2])

location=(18.9582,72.8321)
print('Mumbai Latitude: ',location[0])
print('Mumbai Longitude: ',location[1])
'''
location[0]=12.4567
print(location[0])
'''

def calculate_stats(marks):
    return min(marks), max(marks), sum(marks)/len(marks)
result=calculate_stats((80,45,67,23,85))
print("Minimum: ",result[0])
print("Masximum: ",result[1])
print("Average: ",result[2])

#nested tuple
my_tuple1=("Mouse",[8,1,4],(1,2,5))
print(my_tuple1[2])

n_tuple=("Mouse",[8,1,4],(1,2,5))
print(n_tuple[0][3])
print(n_tuple[1][1])

#Sets
my_set={1,1,1,2,3,4,4,5,6,7,7,8,9,2}
print(my_set)

my_set.add(11)
print(my_set)

print(len(my_set))

for i in my_set:
    print(i)

instagram_user={'Ben','Sagar','Madhvi','Nihal'}
facebook_user={'Ben','Nihal','Maha','Ronak'}
#Common users of both platfomrs - intersection
#Users who use both instagram and facebook
common_user=instagram_user.intersection(facebook_user)
print("Common Users: ",common_user)
#union-all friends
all=instagram_user.union(facebook_user)
print("All Users: ",all)
#Differences - Instagram users only
instagram_only=instagram_user.difference(facebook_user)
print("Instagram Users only: ",instagram_only)
#Differences - Facebook users only
facebook_only=facebook_user.difference(instagram_user)
print("Facebook Users only: ",facebook_only)

#Symmetric differences-exclusive users
#Users only one platform not both
Exclusive=instagram_user.symmetric_difference(facebook_user)
print("Exclusive: ",Exclusive)

set1={"Green","Yellow","Blue"}
set2={"Brown","Black","Blue"}
union=set1.union(set2)
print("Union of the sets are: ",union)
intersection=set1.intersection(set2)
print("Intersection of the sets are: ",intersection)

marketing_students={"MC101","MC202","MC203","MC204","MC205","MC206","MC207","MC209","MC2011","MC2012","MC223","MC222","MC2112"}
data_students={"DS111","MC232","MC103","MC202","MC205","DS206","MC207","DS209","DS2011","MC2012","DS223","MC222","MC2112"}
#total customer list-uniom
union=marketing_students.union(data_students)
