# write program to print patterns as per the picture given in below url. 
# develop separate program for each pattern 
# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png

# 5th one inverted Full Pyramid
#     1 2 3 4 5
# 1   * * * * *
# 2    * * * *
# 3    * * *
# 4     * *
# 5      * 

row=0
col=0
space=0

for row in range(5,0,-1):
    for space in range(row,6):
        print("",end=" ")    
    for col in range(row,0,-1):
        print("*",end=' ')
    row-=1
    print()
    