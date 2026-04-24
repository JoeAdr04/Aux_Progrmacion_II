class Motor:
    def __init__(self, marca, potencia):
        self.__marca = marca
        self.__potencia = potencia
        
    def __str__(self):
        return f"marca: {self.__marca}, potencia:{self.__potencia}"
    
class Carroceria:
    def __init__(self, color, forma):
        self.__color = color
        self.__forma =  forma
    
    def __str__(self):
        return f"color:{self.__color}, forma:{self.__forma}"
    
class Neumatico:
    def __init__(self, numero):
        self.__numeroAro =numero

class Auto:
    def __init__(self, placa, modelo, marca, potencia,color, forma,numero):
        self.__placa = placa
        self.__modelo = modelo
        self.__motor = Motor(marca, potencia)
        self.__carroceria = Carroceria(color, forma)
        self.__n1 = Neumatico(numero)

class Garaje:
    def __init__(self, tamanio, capacidad):
        self.__tamanio = tamanio
        self.__capacidad = capacidad
        self.__autos = []
        
    def agregarAuto(self, a):
        if(len(self.__autos)<= self.__capacidad):
            self.__autos.append(a)
        else:
            print("capacidad superada")

    def getCant(self):
        return len(self.__autos)
    
    def getAutos(self):
        return self.__autos
        
class Edificio:
    def __init__(self, nomb, direccion, garage:Garaje):
        self.__nombre = nomb
        self.__direccion = direccion
        self.__garage = garage
        
    def agregarAuto(self, a):
        self.__garage.agregarAuto(a)
        
        
    def mover(self, otro):
        for a in self.ge
            

class Main():
    
    g1 = Garaje(400, 30)
    g2 = Garaje(600, 50)
    e1 = Edificio("las rosas", "calle falsa", g1)
    e2 = Edificio("natalia", "calle verdadera", g2)
    a1 = Auto(123,"vagoneta", "susuki", 2500, "rojo", "alargado", 42)
    a2= Auto(123,"camioneta", "wolksvagen", 3000, "azul", "alargado", 42)
    a3 = Auto(123,"deportivo", "toyota", 5000, "negro", "alargado", 42)
    a4 = Auto(123,"minibus", "king long", 2000, "blanco", "alargado", 42)
    e1.agregarAuto(a1)
    e1.agregarAuto(a2)
    e2.agregarAuto(a3)
    e2.agregarAuto(a4)
    
    