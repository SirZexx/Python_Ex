# write a program to remove any extra space between words from given string 
# input : apple    banana  mango pinapple
# output apple banana mango pinapple

def remove_extraspaces(string):
    string=string.strip()
    string=string.split()
    print(" ".join(string))
    
remove_extraspaces(input("Enter String :"))
    