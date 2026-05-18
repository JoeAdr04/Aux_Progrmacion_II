'''
Se requiere desarrollar un diagrama de clases para un sistema que administra maratones.Cada 
maraton debe registrar un nombre, la fecha de realizacion, y el lugar donde se llevara acabo.
Cada maraton tiene un unico ORGANIZADOR que es la persona responsable del evento e indispensable
para su realizacion. De este organizador se desea saber su nombre, edad ,genero y numero de telefono
ademas cada maraton tiene una lista de varias carreras. De cada carrera se necesita registrar la hora 
de inicio, la longitud del recorrido y se debe mantener una lista de los CORREDORES inscritos en la
competicion. De cada corredor se desea almacenar su nombre, dedad, genero, y el numero asignado para 
la competicion. Adicionalmente para finalizar cada evento se otorgan medallas a los corredores, por 
lo que se debe considerar tambien en el sistema, cada medalla debe incluir el numero asignado al 
corredor, la categoria y el año en que se otorgo.
Diseña el diagrama de clases correspondiente a este sistema, asi como las relaciones entre ellas.

Problemas para resolver en el laboratorio:
a) Implementar todas las clases con sus respectivos constructores y algun metodo para 
mostrar datos(4 pts.)
b)Instanciar 1 maraton , 2 Carreras  y 4 corredores, ademas de 2 medallas. (2 pts.)
c)Sobrecargar el operador (-) para agregar corredores a una Carrera.(2 pts.)
d) Sobrecargar el operador (+) ara agregare carreras a una maraton. (2 pts.)
e) A cada carrera agregar 2 corredores y agregar las dos carreras a la maraton y mostrar la 
Maraton(2 pts.)
f) Crear un metodo para verificar si en la carrera con longitud de recorrido x se encuentra el coredor 
con nombre y. (2 pts.)
g) Crear un metodo para verifica si en la maraton algun corredor es menor de edad (2 pts.)
h) Crear un metodo para mostrar el nombre de los corredores que ganaron alguna medalla (2 pts.)

i) Crear un metodo que devuelva la cantidad de corredores del genero "femenino" en toda la
Maraton (2 pts.)
'''

class Persona:
    def __init__(self, nom, ed, gen):
        self._nombre = nom
        self._edad = ed
        self._genero = gen
    
    def __str__(self):
        return f"nombre:{self._nombre}, edad:{self._edad}, genero:{self._genero}"
    
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getGenero(self):
        return self._genero
    
class Organizador(Persona):
    def __init__(self, nom, ed, gen, numTel):
        super().__init__(nom, ed, gen)
        self.__numTel = numTel

    def __str__(self):
        return f"{super().__str__()}, numeroTelefono:{self.__numTel}"
    
class Corredor(Persona):
    def __init__(self, nom, ed, gen, numCom):
        super().__init__(nom, ed, gen)
        self.__numComp = numCom
        
    def __str__(self):
        return f"{super().__str__()}, numCompetidor:{self.__numComp}"
    
    def getNum(self):
        return self.__numComp
    
    
    
class Carrera:
    def __init__(self, horaIn, long:int, cor = None):
        self.__horaInicio = horaIn
        self.__longitud = long
        self.__corredores = cor
        if(cor == None):
            self.__corredores = []
        
    def verifica(self, y:str): #parte del inciso f
        for corr in self.__corredores:
            if(y == corr.getNombre()):
                return True
        return False
    
    def getCorredores(self):
        return self.__corredores
            
    def getLongitud(self):
        return self.__longitud
            
    def __str__(self):
        cadena = ""
        for c in self.__corredores:
            cadena = cadena + c.__str__()+"\n"
        return f"horaInicio:{self.__horaInicio}, longitud: {self.__longitud}\nCorredores: \n{cadena}"
    
    def agregaCorredor(self, corr:Corredor): # Main: carrera - corr (__sub__)
        self.__corredores.append(corr)
        
class Maraton:
    def __init__(self, nom, fecha, lug, nomOrg, edad, gen, numTel, carr= None):
        self.__nombre = nom
        self.__fechaRealiza = fecha
        self.__lugar = lug
        self.__organizador = Organizador(nomOrg,edad,gen,numTel)
        self.__carreras = carr
        if(carr == None):
            self.__carreras = []
            
    def __str__(self):
        cadena = ""
        for c in self.__carreras:
            cadena = cadena + c.__str__()+"\n"
        return f"nombre:{self.__nombre}, fecha: {self.__fechaRealiza}, lugar:{self.__lugar}, organizador:{self.__organizador.__str__()} \n{cadena}"
            
    def addCarrera(self, carr:Carrera):
        self.__carreras.append(carr)
        
    #f) Crear un metodo para verificar si en la carrera con longitud de recorrido x se encuentra el coredor  con nombre y. (2 pts.)    
    def verificar(self, x:int, y:str):
        for carr in self.__carreras:
            if(x == carr.getLongitud()):
                if(carr.verifica(y)):
                    return True
                else:
                    return False
        return False
        
    def verificar2(self, x: int,y: str):
        for carr in self.__carreras:
            if(x==carr.getLongitud()):
                corredores = carr.getCorredores()
                for corr in corredores:
                    if(corr.getNombre() == y):
                        return True
                return False
        return False
    
    #g) Crear un metodo para verifica si en la maraton algun corredor es menor de edad (2 pts.)
    def menorEdad(self):
        for carr in self.__carreras:
            corredores = carr.getCorredores()
            for corr in corredores:
                if(corr.getEdad() <18):
                    print(f"el corredor: {corr.getNombre()} es menor de edad")
                    
    #h) Crear un metodo para mostrar el nombre de los corredores que ganaron alguna medalla (2 pts.)
    def verMedalla(self, medallas):
        for carr in self.__carreras:
            corredores = carr.getCorredores()
            for corr in corredores:
                for m in medallas:
                    if(m.getNum() == corr.getNum()):
                        print(corr.getNombre())
                    
    #i) Crear un metodo que devuelva la cantidad de corredores del genero "femenino" en toda la Maraton (2 pts.)
    def contarFem(self):
        cont = 0
        for carr in self.__carreras:
            corredores = carr.getCorredores()
            for corr in corredores:
                if(corr.getGenero() == "femenino"):
                    cont+=1
        return cont
    
class Medalla:
    def __init__(self, num, cat, anio):
        self.__numComp = num
        self.__categoria = cat
        self.__anioEntrega = anio
        
    def __str__(self):
        return f"numComp{self.__numComp}, categoria:{self.__categoria}, anioEntrega:{self.__anioEntrega}"
    
    def getNum(self):
        return self.__numComp
        
class Main():
    print("b)Instanciar 1 maraton , 2 Carreras  y 4 corredores, ademas de 2 medallas. (2 pts.)")
    
    c1 = Corredor("luis", 18, "Masculino", 123)
    c2 = Corredor("ana", 16, "femenino", 312)
    c3 = Corredor("maria", 17, "femenino", 456)
    c4 = Corredor("roy", 19, "femenino", 654)
    
    carr1 = Carrera(8, 10000)
    carr2 = Carrera(9, 8000)
    
    mar = Maraton("Evo", "02-08-2026", "El Alto", "Joel", 27, "Masculino", 69786801)
    
    print("e) A cada carrera agregar 2 corredores y agregar las dos carreras a la maraton y mostrar la Maraton(2 pts.)")
    
    carr1.agregaCorredor(c1)
    carr1.agregaCorredor(c2)
    
    carr2.agregaCorredor(c3)
    carr2.agregaCorredor(c4)
    
    mar.addCarrera(carr1)
    mar.addCarrera(carr2)
    
    print(mar)
    
    print("f) Crear un metodo para verificar si en la carrera con longitud de recorrido x se encuentra el coredor  con nombre y. (2 pts.)")
    
    if(mar.verificar2(8000,"maria")):
        print("encontrado")
    else:
        print("no encontrado")
        
    print("g) Crear un metodo para verifica si en la maraton algun corredor es menor de edad (2 pts.)")
    mar.menorEdad()
    
    print("h) Crear un metodo para mostrar el nombre de los corredores que ganaron alguna medalla (2 pts.)")
    med1 = Medalla(654,"masculino", 2026)
    med2 = Medalla(456,"femenino", 2026)
    medallas = [med1,med2]
    
    mar.verMedalla(medallas)
    
    print("i) Crear un metodo que devuelva la cantidad de corredores del genero femenino en toda la Maraton (2 pts.)")
    print(f"Corredores del genero femenino en la maraton: {mar.contarFem()}")