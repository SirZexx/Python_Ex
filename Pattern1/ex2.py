# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/55984_1580817324.png

# 2nd one Inverted Half Pyramid in numbers

# output
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

row=0
num=0

for row in range(6,1,-1):
    for num in range(1,row):
        print(num,end=" ")
    print()
