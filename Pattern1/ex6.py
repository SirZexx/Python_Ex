# write a program to print following pattern 
# https://i.pinimg.com/474x/bf/9d/ff/bf9dfff6cafa8cbf4f3aa31eb4a3a2d3.jpg

# output
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1 
#  1 5 10 10 5 1 

def factorial(num1):

    count=0
    fact=1
    if num1==1 or num1==0:
        fact==1
    else:
        while count<=num1+1:
            count=count+1
            fact=num1*fact
            num1=num1-1
    
    return fact

# num1=row!/col!(row-col)!

row=space=num=col=0

for row in range(0,6):
    for space in range(row,6):
        print("",end=" ")
    for col in range(0,row+1):
        num=factorial(row)/(factorial(col)*(factorial((row-col))))
        print(int(num),end=' ')
    row+=1
    print()

