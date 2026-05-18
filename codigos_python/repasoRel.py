
#Construir priorizando clases independientes y luego clases padre, por ultimo clases que depoendan de otras.


class Persona: #clase padre priemero la clase padre
    def __init__(self, nom):
        self._nombre = nom
        
    def mostrar(self):
        return f"nombrePersona{self._nombre}"
    
class Docente(Persona): #clases independientes
    def __init__(self, nom,salario, item):
        super().__init__(nom)
        self.__salario = salario
        self.item = item
        
    def mostrar(self):
        return f"{super().mostrar()}"
    
class Estudiante(Persona):
    def __init__(self, nom):
        super().__init__(nom)
        
class Materia:
    def __init__(self, sigla, nom:str, sal:float, it:int, est:Estudiante=None):
        self.__sigla = sigla
        self.__docente = Docente(nom, sal, it)
        self.__estudiantes = []
        if(est == None):
            self.__estudiantes = []
        
    def agregarEstudiante(self, e: Estudiante):
        self.__estudiantes.append(e)
        
class Main():
    
    e1 = Estudiante("joel")
    e5 = Estudiante("luis")
    e4 = Estudiante("maria")
    e3 = Estudiante("luna")
    e2 = Estudiante("tangamandapio")
    
    estudiantes = [e1,e2,e3,e4,e5]
    m1 = Materia("inf111", "jose", 3000, 321, estudiantes)
    e6 = Estudiante("lucas")
    m1.agregarEstudiante(e6)
    
    m2 = Materia("mat126", "zambrana", 5000, 444)
    m2.agregarEstudiante(e5)
    m2.agregarEstudiante(e3)
    m2.agregarEstudiante(e6)