#write a program in python to check whether given string is panindrom or not 
# input : madam 
# reverse : madam 

string=str(input("Enter string to check if its palindrome or not : "))
rev_str=str()
for letter in reversed(string):
    rev_str=rev_str+letter
if rev_str==string:
    print(f"Your string {string} is palindrome string because it's reversed is same as string which is {rev_str} ")
else:
    print(f"Your string {string} is not palindrome string because it's reversed is not same as string which is {rev_str} ")