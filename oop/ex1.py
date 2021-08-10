# write a program to create single level inheritance 
#     parent class kb return KiloBytes of given bytes 
#     child class mb return MegaBytes of given bytes 

class kb():
    def abs(self,bytes):
        if bytes<0:
            return 0-bytes
        else:
            return bytes
    def kb(self,bytes):
        kb=self.abs(bytes)/1024
        return float(kb)
class mb(kb):
    def mb(self,bytes):
        return float(self.kb(bytes) / 1024)

k1=kb()    
bytes=int(input("Enter Bytes to convert it into KiloBytes"))
print(f"{bytes} Bytes is equal to {k1.kb(bytes)} Kb")

m1=mb()
bytes=int(input("Enter Bytes to convert it into MegaBytes"))
print(f"{bytes} Bytes is equal to {m1.mb(bytes)} Mb")
