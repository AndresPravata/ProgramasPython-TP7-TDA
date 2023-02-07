#Ejercicio 3

class Complejo:
    def __init__(self, r1=int, i1=int, r2=int, i2=int):
        self.r1 = r1
        self.i1 = i1
        self.r2 = r2
        self.i2 = i2
        
    def mostraroperaciones (self):
        print (self.r1,"+",self.i1,"i + ",self.r2,"+",self.i2,"i = ",self.r1+self.r2,"+",self.i1+self.i2,"i")
        print (self.r1,"+",self.i1,"i - ",self.r2,"+",self.i2,"i = ",self.r1-self.r2,"+",self.i1-self.i2,"i")
        print (self.r1,"+",self.i1,"i * ",self.r2,"+",self.i2,"i = ",self.r1*self.r2+(self.i1*self.i2)*(-1),"+",self.r1*self.i2+self.i1*self.r2,"i")
        print (self.r1,"+",self.i1,"i / ",self.r2,"+",self.i2,"i = ",self.r1*self.r2-(self.i1*self.i2)*(-1),"/",(self.r2**2)+(self.i2**2),"+",(self.i1*self.r2)-(self.r1*self.i2),"/",(self.r2**2)+(self.i2**2),"i")

r1=int (input("Por favor, ingrese la parte real del primer número "))
i1=int (input("Por favor, ingrese la parte imaginaria del primer número "))
r2=int (input("Por favor, ingrese la parte real del segundo número "))
i2=int (input("Por favor, ingrese la parte imaginaria del segundo número "))
   
complejo1 = Complejo (r1,i1,r2,i2)
complejo1.mostraroperaciones()