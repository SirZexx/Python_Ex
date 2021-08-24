# write a program to remove non dictionary words from given string 
import enchant
def remove_nondictwords(string):
    word=enchant.Dict("en_US")
    string=string.split()
    string1=""
    for element in string:
        if word.check(element)==True:
            print(element,end=" ")
        else:
            string.remove(element)
    
remove_nondictwords(input("Enter String To remove non dictionary Words :"))