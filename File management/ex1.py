# 1 write a program to count words, letters, calculate file size of given file 

import os
file_name=input('Enter File Name :')
file_reader=open(file_name,'r',1)
c_letter=0
c_words=0
for line in file_reader:
    print(line,end="")
    for letter in line:
        c_letter+=1
    line=line.split()
    for word in line:
        c_words+=1
        
print("")
print("-----------------------------------------------")
print("Total Number of Words in given file is : ",c_words)
print("Total Number of Letters in given file is : ",c_letter)
print("Size of file is : ",c_letter)