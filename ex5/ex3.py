date=str(input("Please enter your birth date : ")).zfill(2)  #here .zfill() is inbuilt function which used to add zeros before any number
month=str(input("Please enter your birth month : ")).zfill(2)
dob =month+date     #here i have concatenated two strings
if 12<int(month) or 31<int(date) or 0>int(month) or 0>int(date):   #it's made to give error if month is above 12 and date is above 31 or less than 0
    print("INVALID INPUT")
else:
    dob =int(dob)        #here i have converted that string into integer so we can apply decision making statements
    if 321<=dob<=419:
        print("Your Zodiac Sign is 'Aries' And Your Symbol is 'The Ram' ")
    elif 420<=dob<=520:
        print("Your Zodiac Sign is 'Taurus' And Your Symbol is 'The Bull' ")
    elif 521<=dob<=620:
        print("Your Zodiac Sign is 'Gemini' And Your Symbol is 'The Twins' ")
    elif 621<=dob<=722:
        print("Your Zodiac Sign is 'Cancer' And Your Symbol is 'The Crab' ")
    elif 723<=dob<=822:
        print("Your Zodiac Sign is 'Leo' And Your Symbol is 'The Lion' ")
    elif 823<=dob<=922:
        print("Your Zodiac Sign is 'Virgo' And Your Symbol is 'The Virgin' ")
    elif 923<=dob<=1022:
        print("Your Zodiac Sign is 'Libra' And Your Symbol is 'The Scales' ")
    elif 1023<=dob<=1121:
        print("Your Zodiac Sign is 'Scorpio' And Your Symbol is 'The Scorpion' ")
    elif 1122<=dob<=1221:
        print("Your Zodiac Sign is 'Sagittarius' And Your Symbol is 'The Archer' ")
    elif 1222<=dob<=1231 or 101<=dob<=119:
        print("Your Zodiac Sign is 'Capricorn' And Your Symbol is 'The Goat' ")
    elif 120<=dob<=218:
        print("Your Zodiac Sign is 'Aquarius' And Your Symbol is 'The Water Bearer' ")
    elif 219<=dob<=320:
        print("Your Zodiac Sign is 'Pisces' And Your Symbol is 'The Fishes' ")
    else:
        print("INVALID INPUT")