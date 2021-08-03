# write a program to print first 50 fibonacci number in reverse
count=1
previous=1
current=1
def fibonacci():
    if count<=50:
        next=previous+current
        previous=current
        current=next
        count+=1
        fibonacci(next)
        print(next,end=" ")
        
        
fibonacci()
