# Write a program to findout factorial of given number 
# input = 5
# output = 120
# process = 5 x 4 x 3 x 2 x 1 = 120
# using for loop

num=int(input("Enter the number you want to calculate factorial of : "))
count=0
fact=1
for count in range (0,num+1):
    count=count+1
    if num>=1:
        fact=num*fact
        num=num-1
    # print(num)

print(fact)
