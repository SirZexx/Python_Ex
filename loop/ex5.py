# write a program to print following series (pentagonal  number)
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176 ... 300

n=0
num=0
while num<287:
    num=(n*n-1*n)+(n*n+1*n)/2 #this is formula for pentagonal series
    n+=1
    print(int(num),end=" ")