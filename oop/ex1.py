# write a program to create single level inheritance 
#     parent class kg return KiloBytes of given bytes 
#     child class ton return MegaBytes of given bytes 

class kg():
    def abs(self,bytes):
        if bytes<0:
            return 0-bytes
        else:
            return bytes
    def kg(self,bytes):
        kg=self.abs(bytes)/1024
        return float(kg)
class ton(kg):
    def ton(self,bytes):
        return float(self.kg(bytes) / 1024)

k1=kg()    
bytes=int(input("Enter Bytes to convert it into KiloBytes"))
print(f"{bytes} Bytes is equal to {k1.kg(bytes)} kg")

m1=ton()
bytes=int(input("Enter Bytes to convert it into MegaBytes"))
print(f"{bytes} Bytes is equal to {m1.ton(bytes)} ton")
