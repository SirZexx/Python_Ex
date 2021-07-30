# write a program to convert given decimal number into octal number 

def dec_to_oct(num):
    if num>7:
        # num=num/8
        remainder=num%8
        dec_to_oct(num/8)
        print(int(remainder),end="")
    else:
        print("It's Octagonal Number is :",int(num),end="")
        
        
dec_to_oct(int(input("Enter Number :")))