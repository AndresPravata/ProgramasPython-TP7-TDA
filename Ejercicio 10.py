#Ejercicio 10

class Vehículo:
    def __init__(self,b=int,c=int,d=int,e=int,f=int):
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def moto (self):
        b=50
        print ("Ingrese la marca del Ciclomotor o motocicleta:")
        print ("Ingrese: 1- Honda")
        print ("Ingrese: 2- Corven")
        print ("Ingrese: 3- Zanella")
        print ("Ingrese: 4- Motomel")
        print ("Ingrese: 5- Girela")
        print ("Ingrese: 6- Mondial")
        print ("Ingrese: 7- Keller")
        print ("Ingrese: 8- Bajaj")
        print ("Ingrese: 9- Yamaha")
        print ("Ingrese: 10- Guerrero")

        while b<1 or b>10:
            b=int(input ("Elija una opción: "))

    def auto (self):
         c=50
         print ("Ingrese la marca del auto o camioneta:")
         print ("Ingrese: 1- Toyota")
         print ("Ingrese: 2- Fiat")
         print ("Ingrese: 3- Volkswagen")
         print ("Ingrese: 4- Renaut")
         print ("Ingrese: 5- Peugeot")
         print ("Ingrese: 6- Chevrolet")
         print ("Ingrese: 7- Ford")
         print ("Ingrese: 8- Citroën")
         print ("Ingrese: 9- Nissan")
         print ("Ingrese: 10- Jeep")

         while c<1 or c>10:
             c=int(input ("Elija una opción: "))
             
    def camion (self):
        d=50
        print ("Ingrese la marca del camión:")
        print ("Ingrese: 1- Mercedes Benz")
        print ("Ingrese: 2- Iveco")
        print ("Ingrese: 3- Volkswagen")
        print ("Ingrese: 4- Scania")                                                                      
        print ("Ingrese: 5- Volvo")

        while d<1 or d>5:
            d=int(input ("Elija una opción: ")) 
                
    def colectivo (self):
        e=50
        print ("Ingrese el tipo de transporte de pasajeros:")
        print ("Ingrese: 1- Microbus")
        print ("Ingrese: 2- Buseta")
        print ("Ingrese: 3- Busetón")
        print ("Ingrese: 4- Autobus")
        print ("Ingrese: 5- Servicio de emergencia")

        while e<1 or e>6:
            e=int(input("Elija una opción: "))
                
    def tractor (self):
        f=50
        print ("Ingrese el tipo de maquinaria:")
        print ("Ingrese: 1- Vehiculos con uno o más remolques")
        print ("Ingrese: 2- Maquinaria especial no agrícola")
        print ("Ingrese: 3- Tractores agrícolas")
        print ("Ingrese: 4- Maquinaria especial agrícola")
        print ("Ingrese: 5- Tren agrícola")

        while f<1 or f>5:
            f=int(input ("Elija una opción: "))           
                      

a=50
print ("Ingrese el tipo de vehículo:")
print ("Ingrese: 1- Ciclomotores y motocicletas")
print ("Ingrese: 2- Automóviles y camionetas")
print ("Ingrese: 3- Camiones")
print ("Ingrese: 4- Automotores para servicios de transporte de pasajeros")
print ("Ingrese: 5- Maquinaria")

while a<1 or a>5:
    a=int(input ("Elija una opción: "))
    
if a==1:
    moto1 = Vehículo ()
    moto1.moto ()

if a==2:
    auto1 = Vehículo ()
    auto1.auto ()

if a==3:
    camion1 = Vehículo ()
    camion1.camion ()
    
if a==4:
    colectivo1 = Vehículo ()
    colectivo1.colectivo ()
        
if a==5:
    tractor1 = Vehículo ()
    tractor1.tractor ()