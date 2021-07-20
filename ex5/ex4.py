datem=str(input("Please enter birth date of Male : ")).zfill(2)  #here .zfill() is inbuilt function which used to add zeros before any number
monthm=str(input("Please enter birth month of Male : ")).zfill(2)
dobm =monthm+datem     #here i have concatenated two strings
signm = ""
if 12<int(monthm) or 31<int(datem) or 0>int(monthm) or 0>int(datem):   #it's made to give error if monthm is above 12 and datem is above 31 or less than 0
    print("INVALID INPUT")
else:
    dobm=int(dobm)        #here i have converted that string into integer so we can apply decision making statements
    if 321<=dobm<=419:
        print("Your Zodiac Sign is 'Aries' And Your Symbol is 'The Ram' ")
        signm= "Aries"
    elif 420<=dobm<=520:
        print("Your Zodiac Sign is 'Taurus' And Your Symbol is 'The Bull' ")
        signm="Taurus"
    elif 521<=dobm<=620:
        print("Your Zodiac Sign is 'Gemini' And Your Symbol is 'The Twins' ")
        signm="Gemini"
    elif 621<=dobm<=722:
        print("Your Zodiac Sign is 'Cancer' And Your Symbol is 'The Crab' ")
        signm="Cancer"
    elif 723<=dobm<=822:
        print("Your Zodiac Sign is 'Leo' And Your Symbol is 'The Lion' ")
        signm="Leo"
    elif 823<=dobm<=922:
        print("Your Zodiac Sign is 'Virgo' And Your Symbol is 'The Virgin' ")
        signm="Virgo"
    elif 923<=dobm<=1022:
        print("Your Zodiac Sign is 'Libra' And Your Symbol is 'The Scales' ")
        signm="Libra"
    elif 1023<=dobm<=1121:
        print("Your Zodiac Sign is 'Scorpio' And Your Symbol is 'The Scorpion' ")
        signm="Scorpio"
    elif 1122<=dobm<=1221:
        print("Your Zodiac Sign is 'Sagittarius' And Your Symbol is 'The Archer' ")
        signm="Sagittarius"
    elif 1222<=dobm<=1231 or 101<=dobm<=119:
        print("Your Zodiac Sign is 'Capricorn' And Your Symbol is 'The Goat' ")
        signm="Capricorn"
    elif 120<=dobm<=218:
        print("Your Zodiac Sign is 'Aquarius' And Your Symbol is 'The Water Bearer' ")
        signm="Aquarius"
    elif 219<=dobm<=320:
        print("Your Zodiac Sign is 'Pisces' And Your Symbol is 'The Fishes' ")
        signm="Pisces"
    else:
        print("INVALID INPUT")

#End of male zodiac sign

datef=str(input("Please enter birth date of Female : ")).zfill(2)  #here .zfill() is inbuilt function which used to add zeros before any number
monthf=str(input("Please enter birth month of Female : ")).zfill(2)
signf=""
dobf =monthf+datef     #here i have concatenated two strings
if 12<int(monthf) or 31<int(datef) or 0>int(monthf) or 0>int(datef):   #it's made to give error if monthf is above 12 and datef is above 31 or less than 0
    print("INVALID INPUT")
else:
    dobf=int(dobf)        #here i have converted that string into integer so we can apply decision making statements
    if 321<=dobf<=419:
        print("Your Zodiac Sign is 'Aries' And Your Symbol is 'The Ram' ")
        signf="Aries"
    elif 420<=dobf<=520:
        print("Your Zodiac Sign is 'Taurus' And Your Symbol is 'The Bull' ")
        signf="Taurus"
    elif 521<=dobf<=620:
        print("Your Zodiac Sign is 'Gemini' And Your Symbol is 'The Twins' ")
        signf="Gemini"
    elif 621<=dobf<=722:
        print("Your Zodiac Sign is 'Cancer' And Your Symbol is 'The Crab' ")
        signf="Cancer"
    elif 723<=dobf<=822:
        print("Your Zodiac Sign is 'Leo' And Your Symbol is 'The Lion' ")
        signf="Leo"
    elif 823<=dobf<=922:
        print("Your Zodiac Sign is 'Virgo' And Your Symbol is 'The Virgin' ")
        signf="Virgo"
    elif 923<=dobf<=1022:
        print("Your Zodiac Sign is 'Libra' And Your Symbol is 'The Scales' ")
        signf="Libra"
    elif 1023<=dobf<=1121:
        print("Your Zodiac Sign is 'Scorpio' And Your Symbol is 'The Scorpion' ")
        signf="Scorpio"
    elif 1122<=dobf<=1221:
        print("Your Zodiac Sign is 'Sagittarius' And Your Symbol is 'The Archer' ")
        signf="Sigattarius"
    elif 1222<=dobf<=1231 or 101<=dobf<=119:
        print("Your Zodiac Sign is 'Capricorn' And Your Symbol is 'The Goat' ")
        signf="Capricorn"
    elif 120<=dobf<=218:
        print("Your Zodiac Sign is 'Aquarius' And Your Symbol is 'The Water Bearer' ")
        signf="Aquarius"
    elif 219<=dobf<=320:
        print("Your Zodiac Sign is 'Pisces' And Your Symbol is 'The Fishes' ")
        signf="Pisces"
    else:
        print("INVALID INPUT")
    
#End of female zodiac sign
# print(signm+signf)
sign=signm+signf

favorable =['AriesAries','AriesGemini','AriesLeo','AriesLibra','AriesSagittarius','AriesAquarius',
            'TaurusTaurus','TaurusCancer','TaurusVirgo','TaurusScorpio','TaurusCapricorn','TaurusPisces',
            'GeminiAries','GeminiGemini','GeminiLeo','GeminiLibra','GeminiSagittarius','Aquarius',
            'CancerTaurus','CancerCancer','CancerVirgo','CancerScorpio','CancerCapricorn','CancerPisces',
            'LeoAries','LeoGemini','LeoLeo','LeoLibra','LeoSagittarius','LeoAquarius',
            'VirgoTaurus','VirgoCancer','VirgoVirgo','VirgoScorpio','VirgoCapricorn','VirgoPisces',
            'LibraAries','LibraGemini','LibraLeo','LibraLibra','LibraSagittarius','LibraAquarius',
            'ScorpioTaurus','ScorpioCancer','ScorpioVirgo','ScorpioScorpio','ScorpioCapricorn','ScorpioPisces',
            'SagittariusAries','SagittariusGemini','SagittariusLeo','SagittariusLibra','SagittariusSagittarius','SagittariusAquarius',
            'CapricornTaurus','CapricornCancer','CapricornVirgo','CapricornScorpio','CapricornCapricorn','CapricornPisces',
            'AquariusAries','AquariusGemini','AquariusLeo','AquariusLibra','AquariusSagittarius','AquariusCapricorn','AquariusAquarius',
            'PiscesTaurus','PiscesCancer','PiscesVirgo','PiscesScorpio','PiscesCapricorn','PiscesPisces']
lessfavorable=['AriesTaurus','AriesVirgo','AriesScorpio','AriesPisces',
               'TaurusGemini','TaurusLibra','TaurusSagittarius',
               'GeminiTaurus','GeminiScorpio','GeminiCapricorn',
               'CancerGemini','CancerLeo','CancerSagittarius','CancerAquarius',
               ]
notfavorable=[]

if sign in favorable:
    print('This Couple is Favorable!!!')