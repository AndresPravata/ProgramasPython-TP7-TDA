#Ejercicio 1

class Puntocartesiano:
    def __init__(self, x=float, y=float):
        self.x = x
        self.y = y
        
    def mostrarpunto (self):
        print ("El punto cartesiano creado es: ", (self.x ,self.y))
    
    def modificarpunto (self,a,b):
        self.x = a
        self.y = b
        
x=int (input("Por favor, ingrese el valor de abcisa "))
y=int (input("Por favor, ingrese el valor de ordenada "))     
puntocartesiano1 = Puntocartesiano (x,y)
puntocartesiano1.mostrarpunto()

a=int (input("Por favor, ingrese el valor de abcisa "))
b=int (input("Por favor, ingrese el valor de ordenada "))     
puntocartesiano1.modificarpunto(a,b)
puntocartesiano1.mostrarpunto()