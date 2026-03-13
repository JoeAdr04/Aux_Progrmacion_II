class Pelicula:
    def __init__(self, nombre, duracion, categoria):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__categoria = categoria
        self.actores = []
    
    def addActor(self, x):
        self.actores.append(x)
        
    def mostrarActores(self):
        for x in self.actores:
            print(x)
            
    def __str__(self):
        return f"nombre: {self.__nombre}, duracion: {self.__duracion}, categoria: {self.__categoria}"
    
    def mostrarDuracion(self):
        h = self.__duracion//60
        m = self.__duracion%60
        print(f"duracion de la pelicula= {h}:{m}")
        
    def cambiarCat(self, new):
        self.__categoria = new
        
class CuentaBancaria:
    def __init__(self, titular, nro, saldo):
        self.titular = titular
        self.nroCuenta = nro
        self.saldo = saldo
    
    def __str__(self):
        f"titutlar:{self.titular}, nroCuenta = {self.nroCuenta}, saldo = {self.saldo}"        
        
class Minecraft:
    def __init__(self, nom, dif):
        self.__nombre = nom
        self.__dificultad = dif
        self.__jugadores = []
        self.__diamantes = []
        
    def agregarJugador(self, x):
        self.__jugadores.append(x)
    
class Main():
    p = Pelicula("el aro", 236, "terror")
    p2 = Pelicula("titanes del pacifico", 240, "ficcion")
    p.cambiarCat("comedia")
    p.mostrarDuracion()
    p2.cambiarCat("accion")
    p2.mostrarDuracion()
    p.addActor("silvetre stalone")
    p.addActor("angelina jolie")
    p.addActor("jackie chan")
    p.mostrarActores()