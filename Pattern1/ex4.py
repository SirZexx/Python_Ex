# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/55984_1580817324.png

# 4th one Full Pyramid in numbers

# output
#      1 
#     1 2 
#    1 2 3 
#   1 2 3 4 
#  1 2 3 4 5 
 
row=0
space=0
num=0

for row in range(0,6):
    for space in range(row,6):
        print("",end=" ")    
    for num in range(1,row+1):
        print(num,end=' ')
    row+=1
    print()