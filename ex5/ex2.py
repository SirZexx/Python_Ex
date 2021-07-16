mon_income = int(input("Please enter your monthly income : ")) #Here mon_income is monthly income
y_income = mon_income*12
tax = 1
print("Your Gross Annual Income is : ",y_income)
if y_income>=800000:
    tax=(y_income*30)/100
elif y_income>=500000:
    tax=(y_income*20)/100
elif y_income>=300000:
    tax=(y_income*10)/100    
elif y_income<300000:
    tax = (y_income*5)/100
else:
    print("INVALID NUMBER")
if mon_income>0:
    print("Your Annual Income Tax is : ",tax)
    print("Your Annual Net Income Is : ",y_income-tax)
print("Good Bye...!")