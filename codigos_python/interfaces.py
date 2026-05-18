from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def saludar(self):
        pass
    
    @abstractmethod
    def mostrarEdad(self):
        pass
    
class SerVivo:
    def __init__(self, edad):
        self._edad = edad
        
class Estudiante(SerVivo, Persona):
    def __init__(self, nom, edad):
        super().__init__(edad)
        self.__nombre = nom
        
    def saludar(self):
        return print(f"hola me llamo {self.__nombre}")
    
    def mostrarEdad(self):
        return print(f"mi edad es de {self._edad}")
        
class Main():
    
    e = Estudiante("lUISA", 22)
    e.saludar()
    e.mostrarEdad()