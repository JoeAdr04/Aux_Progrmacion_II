'''
Implementar las clases y los métodos necesarios para resolver los siguientes problemas:
a. (3pts) Crear un objeto pintura que tenga un anuncio y otro objeto pintura sin anuncio
b. (3pts) Mostrar el nombre del artista con más años de Experiencia de ambas pinturas
c. (4pts) Se ha decidido vender la pintura sin anuncio, se pide agregar un anuncio de venta y determine el
monto total de venta de ambas pinturas.
'''

class Anuncio:
    def __init__(self, num, pre):
        self.__numero = num
        self.__precio = pre
        
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, p):
        self.__precio = p
        
class Artista:
    def __init__(self, nom, car, anios):
        self.__nombre = nom
        self.__carnet = car
        self.__anios = anios
        
    def getAniosExp(self):
        return self.__anios
    
    def getNombre(self):
        return self.__nombre

class Obra:
    def __init__(self, titulo, material,nom1, car1,anio1, nom2, car2,anio2, anu=None):
        self._titulo = titulo
        self._material = material
        self._a1 = Artista(nom1, car1, anio1)
        self._a2 = Artista(nom2, car2, anio2)
        self._anuncio = anu
    
    def getTitulo(self):
        return self._titulo
    
class Pintura(Obra):
    def __ini__(self, titulo, material, nom1, car1, anio1, nom2, car2, anio2, gen, anu = None):
        super().__init__(titulo, material, nom1,car1, anio1, nom2, car2, anio2, anu)
        self.__genero = gen
        
    def agregaAnuncio(self, a):
        self._anuncio = a
        
    def compara(self):
        if(self._a1.getAniosExp()>self._a2.getAniosExp()):
            return self._a1
        else:
            return self._a2
        
    def promedio(self):
        return (self._a1.getAniosExp() + self._a2.getAniosExp())/2
    
    def incrementa(self, otro:"Pintura", x1, x2):
        if(self._a1.getNombre() == x2 or self._a2.getNombre() == x2):
            self._anuncio.setPrecio(self._anuncio.getPrecio()+x1)
            print(self.getTitulo())
        elif(otro._a1.getNombre() == x2 or otro._a2.getNombre() == x2):
            otro._anuncio.setPrecio(otro._anuncio.getPrecio()+x1)
            print(otro.getTitulo())
            
    
    def comparaAnios(self, otro:"Pintura"):
        anios1 = self._a1.getAniosExp()
        anios2 = self._a2.getAniosExp()
        anios3 = otro._a1.getAniosExp()
        anios4 = otro._a2.getAniosExp()
        may1 = 0
        nom = ""
        if(anios1 >anios2):
            may1 = self._a1.getAniosExp()
            nom = self._a1.getNombre()
        else:
            may1 = self._a2.getAniosExp()
            nom = self._a2.getNombre()
        may2 = 0
        nom2= ""
        if(anios3 >anios4):
            may2 = otro._a1.getAniosExp()
            nom = otro._a1.getNombre()
        else:
            may2 = otro._a2.getAniosExp()
            nom = otro._a2.getNombre()
            
        #print(f"de la pintura 1:{may1}, de la pintura 2: {may2}")
        if(may1>may2):
            print(nom)
        else:
            print(nom2)
    def montoVenta(self, otra:"Pintura"):
        return self._anuncio.getPrecio() + otra._anuncio.getPrecio()
class Main():
    '''
    #preg 1  Crear un objeto pintura que tenga un anuncio y otro objeto pintura sin anuncio
    p1 = Pintura("monalisa", "oleo", "davincii", 123,10,"joel", 6, 6)
    p2 = Pintura("evo", "acuarela", "cap. lara", 4,5,"linera", 7, 3)
    a = Anuncio(444444, 3000)
    p1.agregaAnuncio(a)
    
    #preg2    b. (3pts) Mostrar el nombre del artista con más años de Experiencia de ambas pinturas
    p1.comparaAnios(p2)
    
    if(p1.compara().getAniosExp()>p2.compara().getAniosExp()):
        print(p1.compara().getNombre())
    else:
        print(p2.compara().getNombre())
        
    
    #pre3 (4pts) Se ha decidido vender la pintura sin anuncio, se pide agregar un anuncio de venta y determine el monto total de venta de ambas pinturas.
    a2 = Anuncio(69786801,120000)
    p2.agregaAnuncio(a2)
    
    print(p1.montoVenta(p2))
    '''
    #a. (3pts) Crear dos objetos pintura que tengan anuncios de venta
    p1 = Pintura("monalisa", "oleo", "davincii", 123,10,"joel", 6, 6)
    p2 = Pintura("evo", "acuarela", "cap. lara", 4,5,"linera", 7, 3)
    a = Anuncio(444444, 3000)
    a2 = Anuncio(69786801,120000)
    p1.agregaAnuncio(a)
    p2.agregaAnuncio(a2)
    
    #(3pts) Calcular el promedio de años Experiencia de los artistas de ambas pinturas
    print(f"promedio{(p1.promedio()+p2.promedio())/2}")
    
    #c. (4pts) Incrementar el precio en X a la pintura del artista con nombre X
    p1.incrementa(p2, 1200,"davincii")
'''
Implementar las clases y los métodos necesarios para resolver los siguientes problemas:
a. (3pts) Crear dos objetos pintura que tengan anuncios de venta
b. (3pts) Calcular el promedio de años Experiencia de los artistas de ambas pinturas
c. (4pts) Incrementar el precio en X a la pintura del artista con nombre X
'''