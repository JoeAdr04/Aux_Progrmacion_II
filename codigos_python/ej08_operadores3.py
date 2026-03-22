from multimethod import multimethod

'''
Sea el contexto de un Cine. Se conoce el nombre del cine, su dirección, la cantidad de las películas en cartelera, un vector con las películas en cartelera, 
un vector con el género de cada película y un vector con el precio de butaca.
a) Implementar la clase cine
b) Instanciar 1 cine con al menos 5 películas en cartelera, y mostrar sus datos
c) Sobrecargar un método para:
i) Mostrar todas las películas del genero comedia.
ii) Mostrar la i-esima película
d) Sobrecargar el operador “++” para incrementar el precio de la butaca en 5 bolivianos.
'''

class Cine:
    def __init__(self, direccion, cant):
        self.__direccion = direccion
        self.__cantPel = cant
        self.__peliculas = []
        self.__genero = []
        self.__precio =[]
        
    def addPelicula(self, nombPel, genero, precio):
        self.__peliculas.append(nombPel)
        self.__genero.append(genero)
        self.__precio.append(precio)
        self.__cantPel = self.__cantPel+1
    
    @multimethod    
    def mostrar(self,x:str):
        for i in range(len(self.__peliculas)):
            print(self.__peliculas[i], self.__genero[i], self.__precio[i])
    
    @multimethod        
    def mostrar(self, i:int):
        print(self.__peliculas[i], self.__genero[i], self.__precio[i])
        
    def __pos__(self):
        for i in range(len(self.__precio)):
            self.__precio[i] = self.__precio[i]+5
        
class Main():
    c = Cine("av. arce", 0)
    c.addPelicula("el aro", "terror", 30.00)
    c.addPelicula("terminator", "ciencia ficcion", 30.00)
    c.addPelicula("lord of the rings", "aventura", 40.00)
    c.addPelicula("spiderman:embargaron la casa", "terror", 10.00)
    c.addPelicula("minecraft", "comedia", 50.00)
    
    c.mostrar("hola")
    c.mostrar(4)
    
    print("---------usando el operador----------")
    +c
    c.mostrar("cualquiera")