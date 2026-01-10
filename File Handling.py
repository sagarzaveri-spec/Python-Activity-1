'''
file=open('hello.txt','r')
print(file.read())
'''

'''
file=open('hello.txt','w')
file.write("Hi there, my name is Sagar. I hope you are having a great day!")
file=open('hello.txt','w')
print(file.read())
file.close()
'''

'''
file=open('hello.txt','a')
file.write("hello everyone")
file=open('hello.txt','r')
print(file.read())
file.close()
'''

'''
file=open('hello.txt','r')
counter=0
content=file.read()
colist=content.split('\n')
for i in colist:
    if i:
        counter+=1
print("These are the number of lines in the file")
print(counter)
'''

file_name='hello.txt'
new_text=input("Enter the text you want to insert: ")+"\n"
print("\nWhere do you want to add the new text?")
print("1. Beginning")
print("2. Middle")
print("3. End")
choice=input("Enter your choice (1/2/3)")
with open(file_name,'r') as file:
    lines=file.readlines()
if choice=='1':
    lines.insert(0,new_text)
elif choice=='2':
    middle_index=len(lines)//2
    lines.insert(middle_index,new_text)
elif choice=='3':
    lines.insert(new_text)
else:
    print("Invalid choice")
with open(file_name,'w') as file:
    file.writelines(lines)
print("File updated successfully!")
with open(file_name,'r') as file:
    print("Updated file context: \n!!!")
    print(file.read())

firstfile=input("Enetr the name of the first file: ")
secondfile=input("Enter the name of the secod file: ")
f1=open(firstfile,'r')
f2=open(secondfile,'r')
print('Contetnt of the first file before appending -\n',f1.read())
print('Contetnt of the second file before appending -\n',f2.read())
f1.close()
f2.close()

f1=open(firstfile,'a+')
f2=open(secondfile,'r')
f1.write(f2.read())
f1.seek(0) #moves the cursor to the mentioned index -- 0 is beginning, 1 is the current position, 2 is end of the file. 
f2.seek(0)
print("Content of the first file after appending -\n",f1.read())
print("Content of the second file after appending -\n",f2.read())
f1.close()
f2.close()