#Ejercicio 6

from datetime import datetime
from datetime import date
from calendar import isleap

dia=0
class Fecha:
    def __init__(self,dia,mes,año):
        self.año = año
        self.mes = mes
        self.dia = dia
        
    def operaciones (self):
        now=datetime.now()
        if año<now.year:
            print ("Han pasado",abs(now.year-año),"años",abs(now.month-mes),"meses",abs(now.day-dia),"días" )
        
        if año>now.year:
            print ("Faltan",abs(now.year-año),"años",abs(now.month-mes),"meses",abs(now.day-dia),"días" )
        
        if año==now.year:
            if mes<now.month:
                print ("Han pasado ",abs(now.month-mes),"meses",abs(now.day-dia),"días" )
            
            if mes>now.month:
                print ("Faltan ",abs(now.month-mes),"meses",abs(now.day-dia),"días" )
            
            if mes==now.month:
                if dia<now.day:
                    print ("Han pasado ",abs(now.day-dia),"días" )
                if dia>now.day:
                    print ("Faltan ",abs(now.day-dia),"días" )
        
dia=50
while (dia<0) or (dia>31):
    dia=int(input("Ingrese el día: "))
    
mes=50   
while (mes<0) or (mes>12):
    mes=int(input("Ingrese el mes: "))
    if (dia==31):
        while (mes==2) or (mes==4) or (mes==6) or (mes==9) or (mes==11):
            mes=int(input("Ingrese el mes: "))                
    if (dia==30):
        while (mes==2):
            mes=int(input("Ingrese el mes: "))

año=int(input("Ingrese el año: "))
if (dia==29) and (mes==2): 
    while isleap(año)==False:
        año=int(input("Ingrese el año: "))

fecha1 = Fecha (dia,mes,año)
fecha1.operaciones ()               