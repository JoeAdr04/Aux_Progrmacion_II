class Persona: #clase padre
    def __init__(self, nom = "", ed = 0,car = 0000):
        self._nombre = nom
        self._edad = ed
        self._carnet =car
        
    def __str__(self):
        return f"nombre:{self._nombre}, edad:{self._edad}, carnet:{self._carnet}"
    
    def getNombre(self):
        return self._nombre
    
class Estudiante(Persona): #clase hija
    def __init__(self, nom="", ed=0, car=0, mat = 000, nota=51):
        super().__init__(nom, ed, car)
        self.__matricula = mat
        self.__nota = nota
        
    def __str__(self):
        return f"nombre:{self._nombre}, edad:{self._edad}, carnet:{self._carnet}, matricula:{self.__matricula}, nota: {self.__nota}"
    def getNombre(self):
        return self._nombre
    
class Maestro(Persona):
    def __init__(self, nom="", ed=0, car=0, horas = 0, materia = "progra1"):
        super().__init__(nom, ed, car)
        self.__horasTrabajo = horas
        self.__materia = materia
    
    def __str__(self):
        return f"{super().__str__()}, horas de trabajo: {self.__horasTrabajo}, materia:{self.__materia}"
    
class Trabajador(Persona):
    def __init__(self, nom="", ed=0, car=0, nit = 0, sindicato = ""):
        super().__init__(nom, ed, car)
        self.__nit = nit
        self.__sindicato = sindicato
        
    def __str__(self):
        return f"{super().__str__}, nit: {self.__nit}, sindicato: {self.__sindicato}"
        
class Main():
    e1 = Estudiante("joel", 123, 456,789, 100)
    print(e1)
    m1 = Maestro("jhon", 321, 654,12,"progra 2")
    print(m1)
    print(e1.getNombre())
    print(m1.getNombre())