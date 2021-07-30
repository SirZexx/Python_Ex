# write a program to print given amount into words 
# input =23456
# output = two three four five six 


words=("zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine")
def num_to_word(n):
    if n<len(amount):
        print(words[amount[n]],end=" ")
        num_to_word(n+1)
    
amount=(input("Enter Amount :"))
amount=list(map(int,amount))
num_to_word(0)