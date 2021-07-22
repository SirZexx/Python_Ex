# print Sum of first 50 numbers divisible by 11

#using for loop
num=0
sum=0
count=1

for count in range(1,51):
    num=num+1
    if num%11==0:
        count=count+1
        sum=sum+num
        
        
print(f"Sum of first 50 numbers divisible by 11 is {sum}.")

# not solved