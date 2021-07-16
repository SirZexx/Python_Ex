e_units=int(input("please enter your monthly electricity units : ")) #Here e_units is monthly units used by user
e_bill= 1
if e_units>=400:
    e_bill=e_units*5
elif e_units>=300:
    e_bill=e_units*4    
elif e_units>=200:
    e_bill=e_units*3
elif e_units>=100:
    e_bill=e_units*2
elif e_units>0:
    e_bill=e_units*1
else:
    print("INVALID units")
energy_charge=(e_bill * 5 )/100
if e_units>0:
    print("Your energy charge is : ", energy_charge)
    print("Your net electricity bill is : ",e_bill)
    e_bill=e_bill+energy_charge
    print("Your TOTAL electricity bill is : ",e_bill)
print("Goode Bye...!")
