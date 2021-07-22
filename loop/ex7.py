# write a program to print 1st 10 number as per  The Lazy Caterer’s Sequence

n=0
num=0
count=1
while count<11:
    count+=1
    num=(n*n+n+2)/2 #this is formula for The Lazy Caterere's Sequence
    n+=1
    print(int(num),end=" ")