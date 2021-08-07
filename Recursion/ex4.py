# write a program to print first 50 fibonacci number in reverted
previous=0
current=1
count=0
def fibonacci(next):
    global count
    global current
    global previous
    if count<=50:
        next=current+previous
        previous=current
        current=next
        count+=1
        fibonacci(count)
    print(next,end=" ")

fibonacci(0)