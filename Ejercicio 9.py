#Ejercicio 9

import math

math.pi

class Circulo:
    def __init__(self, r=float):
        self.r=r
                    
    def operaciones (self):
        print ("La longitud del círculo es: ", (2 * math.pi * r))
        print ("La superficie del círculo es: ", (math.pi * r**2))
        
r=float (input("Por favor, ingrese el radio del círculo "))


circulo1 = Circulo (r)
circulo1.operaciones ()          