rbs = int(input("Please Enter Your RBS "))
eat = bool(input("This Result is After Eating? (True or False) "))
if 175<=rbs<=185 and eat==True:
    print("You have a normal RBS!!")
if rbs<=174 and eat==True:
    print("You Do Not Have A Normal RBS!!")
if 186<=rbs and eat==True:
    print("You Do Not Have A Normal RBS!!")
if 80<=rbs<=130 and eat==False:
    print("You have a normal RBS!!")
if rbs<=79 and eat==False:
    print("You Do Not Have A Normal RBS!!")
if 131<=rbs and eat==False:
    print("You Do Not Have A Normal RBS!!")

    