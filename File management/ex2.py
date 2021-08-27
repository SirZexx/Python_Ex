# 2 write a program to print every alternate word of given file 

import os

file_name=input("Enter File name : ")
file_reader=open(file_name,"r",1)
count=1
for line in file_reader:
    line=line.split()
    for word in line:
        count+=1
        if count%2==0:
            print(word,end=" ")
        