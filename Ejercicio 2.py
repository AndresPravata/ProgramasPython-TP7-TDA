#Ejercicio 2

class Recta:
    def __init__(self, a=float, b=float):
        self.a = a
        self.b = b
        
    def mostrarrecta (self):
        print ("La recta creada es: y = ", self.a ,"x +",self.b)
        
a=int (input("Por favor, ingrese el valor de la pendiente "))
b=int (input("Por favor, ingrese el valor de la ordenada al origen ")) 
    
recta1 = Recta (a,b)
recta1.mostrarrecta()