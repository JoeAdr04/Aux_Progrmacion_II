#asbtarccion
##crear una clase, encapsulamiento, getters, setters. funciones
#from multimethod import multimethod
class Persona:
    def __init__(self, n):
        self._nombre = n
    
#polimorfismo
#override(sobreescribir), overload(sobrecargar) - mismo nombre de funcion, difernetes aprametros de entrada
    #@multimethod
    def saludar(self):
        print("hola")
        
    #@multimethod    
    def saludar(self, x):
        print(f"hola{x}")

#operadores ! 
    def __sub__(self, x):
        return self.__nombre+x
    
#herencia
# es un, es una, clase pasdre clase hija.}

class Estudiante(Persona):
    def __init__(self, n, e):
        super().__init__(n)
        self.__edad = e
        
    def saludar(self, x):
        return self._nombre
##interfaces(define metodos) y clases abstractas
#asociascion(establecer multiplicidad, asociar)

#agregacion
class Curso:
    def __init__(self, n):
        self.estudiantes = []
        self.maestro = Persona(n)#composicion
        
    def addEstudiante(self, e):#agregacion
        self.estudiantes.append(e)
#composicion
#genericidad

#excepciones
#persistencia
class Main():
    p = Persona(2)
    #x =p-3
    #print(x)
    e = Estudiante("roy", 12)
    c = Curso("jose luis")
    c.addEstudiante(e)
    try:
        print(5/1)
    except ZeroDivisionError:
        print("dicision entre cero")
    finally:
        print("simepre pasa")