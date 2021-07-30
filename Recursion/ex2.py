# write a program to convert given decimal number into hexadecimal number 

hex=(0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F")
def dec_to_hex(num):
    if num>=1:
        remainder=num%16
        dec_to_hex(num/16)
        print(hex[int(remainder)],end="")
    else:
        print("It's Hexadecimal Number is :",end=" ")
        
dec_to_hex(int(input("Enter Number :")))