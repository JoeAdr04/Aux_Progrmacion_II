from abc import ABC, abstractmethod

class Persona(ABC):

    def saludar(self):
        pass
    

    def mostrarEdad(self):
        pass
    
class SerVivo:
    def __init__(self, edad):
        self._edad = edad
        
class Estudiante(SerVivo, Persona):
    def __init__(self, nom, edad):
        super().__init__(edad)
        self.__nombre = nom
        

class Main():
    
    e = Estudiante("lUISA", 22)
    p = Persona()
    #e.saludar()
    #e.mostrarEdad()