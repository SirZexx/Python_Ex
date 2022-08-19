t=50000 #starting balance
for k in range (0,3): #total years of trading
    k=+1
    for j in range(0,12): #months of trading in specific year
        j=+1
        for i in range(0,15): #days of trading in specific month
            if i%2==0:
                rt=t/100 #1% return per day
            else:
                rt=t/400 # 0.25% return per day
            t=t+rt
            print(t)
        t=t+5000 # balance i'll be adding to my total balance every month
    t=t+20000 #balance i'll be adding to ma=y total balance every year      