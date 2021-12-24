class Parent():
      def add(self,a,b):
          return a+b 
      def sub(self,c,d):
           return c-d 
class child(Parent):
      def mul(self,e,f):
          return e*f 
      def div(self,g,h): 
          return g/h


inst=child()
print(inst.mul(3,2))
print(inst.div(8,4))
print(inst.add(1,2))
print(inst.sub(10,5))
 