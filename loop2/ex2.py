#write a program to accept one line from user and count how many repetitive words it has 
# input: india is largest country in population. india is also 5th largest country area wise 
# output 
# india 2 
# is 2
# country 2 
# largest 2

line=input("Enter Line to count repetitive words in it. : ")
line=line.lower()
line=list(line.split())
