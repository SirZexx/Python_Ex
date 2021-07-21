# Write a program to make sum of first 50 numbers which are divisible by 11 and also display it on screen

# using While loop

count=0
sum=0
num=0

while count<=50:
    num = num +1
    if num%11==0:
        sum=sum+num
        count = count + 1
print(f"Sum of first 50 numbers which are divisible by 11 is {sum}.")