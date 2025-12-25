'''
my_list=[]
my_list2=[1,2,3,4,5]
my_list3=[1,2,4.9,5,"list",6,7,8,9]
print(len(my_list3))

#indexing
print(my_list3[4])

#slicing
new_list=my_list3[1:4]
print(new_list)

#add items
my_list3.append('Python')
print(my_list3)

#remove items
my_list3.remove(4.9)
print(my_list3)
#pop removes the last item in this list.
my_list3.pop()
print(my_list3)

for i in my_list3:
    print(i)

a_list=['Apple','Guava','Mango','Banana']
print("Length of the list",len(a_list))

#Sort makes it alphabetical A-Z
a_list.sort()
print(a_list)

#It gives the list from Z-A
a_list.reverse()
print(a_list)

#clear deletes the entire list
a_list.clear()
print(a_list)
'''

marks=[78,95,23,89,00]
average=sum(marks)/len(marks)
print("Average Marks: ",average)

emails=['xyz@gmail,.com','abc@yahoo.com','user1@codingal.com']
if 'user1@codinal.com' in emails:
    print('User exists')
else:
    print("Does not exist")

Salaries=[100000,399210,29292,1122,449]
print("Maximum salary is",max(Salaries))

#Nested Lists
revised_marks=[[81,90,92,21,22,99],[29,11,23,45,66,77],[19,99,24,66,78,90]]
print(revised_marks[0])
print(revised_marks[1][2])
print(revised_marks[2][3])
for student in revised_marks:
    print(student[0])

#dictionary
my_dict={}
my_dict1={'Name':'Sagar','Language1':'Marathi','Language2':'Gujarati'}
print(my_dict1)
print(len(my_dict1))

#update value
my_dict1['Name']="Mansi"
print(my_dict1)

#add item to dictionary
my_dict1['Gender']='Female'
print(my_dict1)

#remove the particular element
my_dict1.pop('Name')
print(my_dict1)

#access a particular element
print("First Language: ",my_dict1.get('Language1'))

def test(first_list):
    Result={}
    for item in first_list:
        Result[item[0]]=item[1:]
    return Result

students=[[1,'Jean Castro','V'],[2,'Lula Powell','V'],[3,'Howard Powell','IV'],[4,'Sheldon Cooper','VI']]

print('\nOriginal list of lists: ')
print(students)
print("\nConverted lists to a dictionary: ")
print(test(students))