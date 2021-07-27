# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/55984_1580817324.png

# 5th one Hollow Inverted half Pyramid in numbers

# output
# 1 2 3 4 5 
# 1     4 
# 1   3 
# 1 2
# 1

row=0
num=0

for row in range(5,0,-1):
    for num in range(1,row+1):
        if row==3 and num==2:
            print(" ",end=" ")
        elif row==4 and num==2:
            print(" ",end=" ")
        elif row==4 and num==3:
            print(" ",end=" ")
        else:
            print(num,end=" ")
    print()