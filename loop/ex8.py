# write a program to print 1st 10 number as per  Magic Square series

n=0
num=0
count=1
while count<11:
    count+=1
    num=(n*n*n+n)/2 #this is formula for Magic Square Series
    n+=1
    print(int(num),end=" ")