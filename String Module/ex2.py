# write a program to reverse each word in given string 
# input : apple banana mango 
# output : elppa ananab ognam 

def reverse(string):
    line=""
    string1=""
    for letter in string:
        line=letter+line
    line=line.split()
    # print(line)
    for count in range(len(line)):
        string1=str(line[count:count+1])+string1
    string1="".join(string1)
    print(str(string1))
    
reverse(input("Enter String : "))