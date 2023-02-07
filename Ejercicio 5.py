#Ejercicio 5

class Racional:
    def __init__(self,p=int,q=int):
        self.p = p
        self.q = q
        
    def fraccion (self):
        print ("El número que se ha formado es: ",p,"/",q," = ",(p/q))

p=int (input("Por favor, ingrese el numerador "))

q=0
while q==0:
    q=int (input("Por favor, ingrese el denominador "))
   
racional1 = Racional (p,q)
racional1.fraccion ()