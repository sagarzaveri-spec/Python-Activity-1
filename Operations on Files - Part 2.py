with open('hello.txt','w') as file:
    file.write("Hello! I am a Penguin and I am 2 years old")
file.close()

with open('hello.txt','r') as file:
    data=file.readlines()
    print('Words in this file are...')
    for line in data:
        word=line.split()
        print(word)
file.close()

'''
#Create a new file
file=open('New Document.txt','x')
'''

'''
new_file=open('New_File.txt','x')
new_file.close()

# check if a file exists
import os
print("Checking if the file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove('my_file.txt')
else:
    print("The file does not exist")
# create a new if it does not exist
my_file=open('New_File.txt','w')
my_file.write("Hi! My name in Pemguin and I am 22 years old")
my_file.close()

# To remove the entire folder
# os.rmdir('Folder')

'''

OutputFile=open('Updated_File.txt','w')
InputFile=open('Repeated.txt','r')

lines_seen_already=set()
print("Elimintaing Duplicate Lines...")
for line in InputFile:
    if line not in lines_seen_already:
        OutputFile.write(line)
        lines_seen_already.add(line)
InputFile.close()
OutputFile.close()