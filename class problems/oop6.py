#example of multilevel inheritance 
class foot():
    def __init__(self,inch):
        self.inch = inch
        print("foot class constructor is called")
    def getfoot(self):
        return self.inch /12
class meter(foot):
    def __init__(self,inch):
        self.inch=inch
        foot.__init__(self,inch) #calling parent class constructor
        print("meter class constructor is called")
    def getmeter(self):
        return self.getfoot()/ 3.28
class km(meter):
    def __init__(self,inch):
        self.inch = inch
        meter.__init__(self,inch) #calling parent class constructor
        print("km class constructor is called")
    def getkm(self):
        return self.getmeter()/1000
    
inch = float(input("enter inches"))
k1 = km(inch)
print("Kilometer = ",k1.getkm())
print("meter = ",k1.getmeter())
print("foot = ",k1.getfoot())