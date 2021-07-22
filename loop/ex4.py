# write a program to print following series (triangular numbers)
# 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... 1000

previous=0
current=1
position=1
print(previous)

while current<=990:
    current=previous+position
    print(current,end=" ")
    previous=current
    current+=1
    position+=1