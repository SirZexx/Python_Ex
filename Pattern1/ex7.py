# write a program to print following pattern 
# https://i.pinimg.com/236x/d9/95/9d/d9959d1d28c25fe04109c3141e9828b1.jpg

# output
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 6 5 4 3 2 1 
#       1 2 3 4 5 6 5 4 3 2 1 
#         1 2 3 4 5 4 3 2 1 
#           1 2 3 4 3 2 1 
#             1 2 3 2 1 
#               1 2 1 
#                 1 

row=0
space=0
num=0

for row in range(9,0,-1):
    for space in range(row,9):
        print("",end="  ") 
    for num in range(1,row+1):
        print(num,end=' ')
    for num in range (row-1,0,-1):
        print(num,end=' ')
        num+=1
    row+=1
    print()