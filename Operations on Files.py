'''
file=open('hello.txt','r')
print(file.read(12))
print(file.readline())
print(file.readline())
print(file.readline())

for x in file:
    print(x)

file.close()
'''

'''
file1=open('hello.txt','r')
file2=open('Contacts.txt','w')
for line in file1.readlines():
    if not(line.startswith('Hello')):
        print(line)
        file2.write(line)
file1.close()
file2.close()
'''

file1=open('hello.txt','r')
file2=open('Contacts.txt','w')
cont=file1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i%2!=0):
        file2.write(cont[i-1])
    else:
        pass
file2.close()
file2=open('Contacts.txt','r')
cont1=file2.read()
print(cont1)
file1.close()
file2.close()