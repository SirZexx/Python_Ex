# write a program to find out and remove repetitive words from given string and display it on screen 
import string
def repetitive_words(line):
    line=line.split()
    repeat=0
    for count in range(len(line)):
        word=line[count:count+1]
        if (word in line):
            
            line.remove(word)
        print(word)
    
    
    

    
repetitive_words(input("Enter String :"))
    