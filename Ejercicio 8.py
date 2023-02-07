#Ejercicio 8

class Rectangulo:
    def __init__(self, b=float, h=float):
        self.b = b
        self.h = h
        
    def operaciones (self):
        print ("El perímetro del rectángulo es: ", 2*b+2*h)
        print ("La superficie del rectángulo es: ", b*h)
        
b=float (input("Por favor, ingrese la base del rectángulo "))
h=float (input("Por favor, ingrese la altura del rectángulo "))

rectangulo1 = Rectangulo(b,h)
rectangulo1.operaciones()               