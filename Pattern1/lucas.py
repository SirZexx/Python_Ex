# write a program to print following series (Lucas series)
# 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123 .... 300

num=0
current=1
previous=2
next=0
print(previous,end=" ")

while current<300:
    next=current+previous
    previous=current+previous
    current=previous
    print(next,end=" ")
