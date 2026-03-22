'''
Sea la clase celular (nroTel, dueño, espacio, ram, nroApp)
a) Realizar el diagrama de clases
b) Realizar la sobrecarga del operador ++ para aumentar en 10 el nroApp.
c) Realizar la sobrecarga del operador - - para disminuir el espacio en 5 gb.
d) Mostrar los datos antes y después de los operadores.
'''

class Celular:
    def __init__(self, nroTel=0, duenio="", espacio=256, ram=8,nroApp=0):
        self.__nroTel = nroTel
        self.__duenio = duenio
        self.__espacio = espacio
        self.__ram = ram
        self.__nroApp = nroApp
        
    def __pos__(self):
        self.__nroApp = self.__nroApp+10
        
    def __add__(self, other):
        if(isinstance(other,int)):
            self.__nroApp = self.__nroApp+other
        elif(isinstance(other,str)):
            self.__duenio = other
        elif(isinstance(other,Celular)):
            return Celular(0,self.__duenio,256,8,other.__nroApp)
        
    def __neg__(self):
        self.__espacio = self.__espacio-5
        
    def __str__(self):
        return f"nro:{self.__nroTel}, duedio:{self.__duenio}, espacio:{self.__espacio}, ram:{self.__ram}, nroApp: {self.__nroApp}"
class Main():
    
    c = Celular()
    print("antes")
    print(c)
    +c
    -c
    #c+20
    
    print("despues")
    print(c)
    
    c+"joel"
    print("despues 2")
    print(c)
    
    print("Sumando dos objetos")
    c2 = Celular(123,"LUIS",128,4,15)
    c3 = c+c2
    print(c3)
    