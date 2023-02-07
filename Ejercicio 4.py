#Ejercicio 4

class Logico:
    def __init__(self,a=bool,b=bool):
        self.a = a
        self.b = b

    def mostraroperaciones (self):
        a=False
        b=True
        
        print ("NOT")
        print ("NOT ",a, " = ", not a)
        print ("NOT ",b, " = ", not b)
        
        print ("AND - Y")
        print (a, " Y ",a, " = ", a and a)
        print (a, " Y ",b, " = ", a and b)
        print (b, " Y ",a, " = ", b and a)
        print (b, " Y ",b, " = ", b and b)
        
        print ("Or - O")
        print (a, " O ",a, " = ", a or a)
        print (a, " O ",b, " = ", a or b)
        print (b, " O ",a, " = ", b or a)
        print (b, " O ",b, " = ", b or b)
        
        print ("NOR")
        print (a, "NOR",a, " = ", b)
        print (a, "NOR",b, " = ", a)
        print (b, "NOR",a, " = ", a)
        print (b, "NOR",b, " = ", b)

        print ("XOR")
        print (a, "NOR",a, " = ", a)
        print (a, "NOR",b, " = ", b)
        print (b, "NOR",a, " = ", b)
        print (b, "NOR",b, " = ", a)        
        

logico1 = Logico()
logico1.mostraroperaciones()    
