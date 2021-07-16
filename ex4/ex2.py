day = str(input("Please enter the name of day you want to know CHOGHADIYA of ex, Monday,Tuesday : "))

sun={'Day' : 'Udveg , Chal , Labh , Amrit , Kaal , Shubh , Rog , Udveg ' , 'Night' : 'Shubh , Amrit , Chal , Rog , Kaal , Labh , Udveg , Shubh '}
mon={'Day' : 'Amrit , Kaal , Shubh , Rog , Udveg , Chal , Labh , Amrit' , 'Night' : 'Chal , Rog , Kaal , Labh , Udveg , Shubh , Amrit , Chal '}
tue={'Day' : 'Rog , Udveg , Chal , Labh , Amrit , Kaal , Shubh , Rog' , 'Night' : 'Kaal , Labh , Udveg , Shubh , Amrit , Chal , Rog , Kaal '}
wed={'Day' : 'Labh , Amrit , Kaal , Shubh , Rog , Udveg , chal , Labh' , 'Night' : 'Udveg , Shubh , Amrit , Chal , Rog , Kaal , Labh , Udveg '}
thu={'Day' : 'Shubh , Rog , Udveg , Chal , Labh , Amrit , Kaal , Shubh' , 'Night' : 'Amrit , Chal , Rog , Kaal , Labh , Udveg , Shubh . Amrit '}
fri={'Day' : 'Chal , Labh , Amrit , Kaal , Shubh , Rog , Udveg , Shubh' , 'Night' : 'Rog , Kaal , Labh , Udveg , Shubh , Amrit , Chal , Rog '}
sat={'Day' : 'Kaal , Shubh , Rog , Udveg , Chal , Labh , Amrit , Chal' , 'Night' : 'Labh , Udveg , Shubh , Amrit , Chal , Rog , Kaal , Labh '}

if day=="Sunday" or day=="sunday" :
    print("Sundays Choghadiya are " ,sun)
elif day=="Monday" or day=="monday":
    print("Mondays Choghadiya are ",mon)
elif day=="Tueday" or day=="tuesday":
    print("Tuedays Choghadiya are ",tue)
elif day=="Wednesday" or day=="wednesday":
    print("Wednesdays Choghadiya are ",wed)
elif day=="Thursday" or day=="thursday":
    print("Thursdays Choghadiya are ",thu)
elif day=="Friday" or day=="friday":
    print("Fridays Choghadiya are ",fri)
elif day=="Saturday" or day=="saturday":
    print("Saturdays Choghadiya are ",sat)
else :
    print('Please print valid Day')
