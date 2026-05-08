from abc import ABC, abstractclassmethod
class Motor:
    def __init__(self, potencia):
        self._potencia = potencia
    def __str__(self):
        return f"potencia:{self._potencia}"
    def getPotencia(self):
        return self._potencia

class Vehiculo(ABC):
    def __init__(self, marca, modelo, precio, potencia):
        self._marca = marca
        self._modelo = modelo
        self._precio = precio
        self._motor = Motor(potencia)
        
    def __str__(self):
        return f"marca:{self._marca}, modelo:{self._modelo}, precio:{self._precio}, motor:{self._motor}"
    
    def getModelo(self):
        return self._modelo
    def getPrecio(self):
        return self._precio
    def setPrecio(self, p):
        self._precio = p
    def getPotencia(self):
        return self._motor.getPotencia()
    def getMarca(self):
        return self._marca
    def getModelo(self):
        return self._modelo
class Auto(Vehiculo):
    def __init__(self, marca, modelo,precio, potencia, puertas):
        super().__init__(marca, modelo, precio, potencia)
        self.__puertas = puertas
        
    def __str__(self):
        return f"{super().__str__()}, puertas:{self.__puertas}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio, potencia, cilindrada):
        super().__init__(marca, modelo,precio, potencia)
        self.__cilindrada = cilindrada
    def __str__(self):
        return f"{super().__str__()} cilindrada:{self.__cilindrada}"
    
class Gerente:
    def __init__(self, nombre, carnet, nit, concesionario = None):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__nit = nit
        self.__concesionario = concesionario
    
    def getConcesionario(self):
        return self.__concesionario
    
    def setConcesionario(self, concesionario):
        self.__concesionario = concesionario
        
    def __str__(self):
        return f"nombre:{self.__nombre}, carnet:{self.__carnet}, nit:{self.__nit}"
    
    def masIngresos(self, otro:"Gerente"):
        if(self.__concesionario.getIngresos()> otro.__concesionario.getIngresos()):
            print(f"Gerente con mas ingresos: {self}")
        else:
            print(f"Gerente con mas ingresos: {otro}")
            
    def agotaStock(self, otro:"Gerente"):
        if(self.__concesionario.getStock() == 0 and otro.__concesionario.getStock() !=0):
            print(f"Gerente sin stock: {self}")
        elif(self.__concesionario.getStock() != 0 and otro.__concesionario.getStock()   ==0):
            print(f"Gerente sin stock: {otro}")
        elif(self.__concesionario.getStock() == 0 and otro.__concesionario.getStock() ==0):
            print("ambos gerentes quedaron sin stock")
        else:
            print("ambos gerentes aun tienen stock")
class Concesionario:
    def __init__(self, nombre, gerente = None, vehiculos = None):
        self.__nombre = nombre
        self.__gerente = gerente
        self.__stock = 0
        self.__ingresos = 0
        self.__vehiculos = []
        
    def getNombre(self):
        return self.__nombre
    
    def getIngresos(self):
        return self.__ingresos
    
    def getStock(self):
        return self.__stock
        
    def setGerente(self, gerente:Gerente):
        self.__gerente = gerente
        if(gerente != None and gerente.getConcesionario() != self):
            gerente.setConcesionario(self)
        
    def __str__(self):
        lista = ""
        for v in self.__vehiculos:
            lista = lista + v.__str__()+ "\n"
        return f"nombre:{self.__nombre},stock:{self.__stock} gerente:{self.__gerente}\n{lista}"
    
    def addVehiculo(self, v):
        self.__vehiculos.append(v)
        self.__stock = self.__stock +1
        
    def aplicaDesc(self): #fila a
        for v in self.__vehiculos:
            if(v.getModelo()<2022):
                v.setPrecio(v.getPrecio()*0.85)
    
    def aplicaDesc(self): #fila b
        for v in self.__vehiculos:
            if(v.getModelo()>2022):
                v.setPrecio(v.getPrecio()*0.83)
                
    def aumentaPrecio(self):
        for v in self.__vehiculos:
            if(v.getPotencia()>3000):
                v.setPrecio(v.getPrecio()*1.05)
                
    def vender(self, marc, mod):
        for v in self.__vehiculos:
            if(v.getMarca() ==marc and v.getModelo() == mod):
                self.__vehiculos.remove(v)
                self.__stock = self.__stock-1
                self.__ingresos = self.__ingresos+v.getPrecio()
                
        
    
class Main():
    a1 = Auto("susuki", 2026,16000, 3000, 4)
    a2 = Auto("toyota", 2025,23000, 5000, 2)
    a3 = Auto("hilux", 2025,23000, 5000, 2)
    m1 = Moto("toyota",2020,15000, 1500, 150)
    m2 = Moto("pegasus",2024,12000, 1000, 120)
    m3 = Moto("xiaomi",2024,12000, 1000, 120)
    
    con = Concesionario("veloz")
    con2 = Concesionario("imcruz")
    ger = Gerente("juan luis guerra",12341234, 4321)
    ger2 = Gerente("Pedro perez pereira",12341234, 4321)
    con.setGerente(ger)
    con2.setGerente(ger2)
    
    con.addVehiculo(a1)
    con.addVehiculo(a2)
    con.addVehiculo(m3)
    con2.addVehiculo(m1)
    con2.addVehiculo(m2)
    con2.addVehiculo(a3)
    
    con.aplicaDesc()
    con2.aplicaDesc()
    
    con.aumentaPrecio()
    con2.aumentaPrecio()
    print(con)
    print(con2)
    con.vender("toyota", 2025)
    con2.vender("xiaomi", 2024)
    
    print(con)
    print(con2)
    
    ger.masIngresos(ger2)
    ger.agotaStock(ger2)

#crea dos consecionarios con almenos 3 vehiculos cada uno (implementar las clases consecionario, vehiculo y gerente)
#crea la funcion aplkicar descuento del 15% a los vehiculos de modelos con mas de 4 años de antiguedad
#aumenta un 5% al precio de los vehiculos cuya potencia sea mayor a 3000
#realiza la funcin para hacer una venta y realiza 3 ventas en los distitntos consesionarios
#mustra cual de los gerentes ha realizado mayor numero de ingresos en sus consecionario