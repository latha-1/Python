class details:
    def __init__(self,var1,var2): #constructor
        self.var1=var1 
        self.var2=var2 
        
    def add(self,a,b):
        return self.var1+self.var2+a+b 
        
        
inst=details(3,2)
print(inst.add(1,2))