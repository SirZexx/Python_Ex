# write a program to print following series (hexagonal number)
# 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231 .. 1000

n=0
num=0
while num<946:
    num=2*n*n-n #this is formula for Hexagonal series
    n+=1
    print(int(num),end=" ")