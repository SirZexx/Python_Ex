# write a program to create single level inheritance 
#     parent class kilo return KG of given grams 
#     child class ton return ton of given grams 

class kg():
    def abs(self,grams):
        if grams<0:
            return 0-grams
        else:
            return grams
    def kg(self,grams):
        kg=self.abs(grams)/1000
        return float(kg)
class ton(kg):
    def ton(self,grams):
        return float(self.kg(grams) / 1000)

k1=kg()    
grams=int(input("Enter grams to convert it into Kilograms : "))
print(f"{grams} grams is equal to {k1.kg(grams)} kg")

m1=ton()
grams=int(input("Enter grams to convert it into Megagrams : "))
print(f"{grams} grams is equal to {m1.ton(grams)} ton")