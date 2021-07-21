# 2) write a program to print 1 to 5 multiplication table using single loop 

num=1
count=1
multiplication=1

for count in range(1,12):
    if count<=11:
        multiplication=count*num
        print(f"{num} x {count} = {multiplication}")
    elif count>11:
        count=1
        num=num+1
               

