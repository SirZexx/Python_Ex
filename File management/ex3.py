# 3 write a program to findout given word exist in given file or not. if found print line and it's line number

import os

file_name=input("Enter File name : ")
file_reader=open(file_name,'r',1)
word=input("Enter Word that you would like to know if it exists in file or not : ")
count=0
word_count=0
for line in file_reader:
    count+=1
    line1=line.split()
    if word in line1:
        word_count+=1
        print(f"Word {word} Exists in given file on line {count}")
        print("Line is : ",line)
        
if word not in line1 and word_count==0:
    print(f"given word {word} does not exist in given file {file_name}")