# 1) write a program to count words,vowels,digits,consonant,spaces,symbols  in given string 

word=vowel=digit=consonant=space=symbol=0
line=input("Enter Line of which you want to count words,vowels,digit,consonants,spaces,symbols. : ")
line=line.upper()   #converting user inputted string into uppercase character for efficient programming
for letter in line:
    letter=ord(letter)    #here i've used ord() function which gives you values of given character into ascii value
    if 65<=letter<=90:
        consonant+=1
        if letter==65 or letter==69 or letter==73 or letter==79 or letter==85:
            vowel=vowel+1
    elif 48<=letter<=57:
        digit = digit+1
    elif letter==32:
        space=space+1
    else:
        symbol=symbol+1
        
print(f"Vowels = {vowel} , Consonants = {consonant} , Digits = {digit} , Words = {space+1} , Spaces = {space} , Symbols = {symbol}")
        