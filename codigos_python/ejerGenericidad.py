from typing import Generic, TypeVar

T = TypeVar('T')

class Espada:
    def __init__(self, dan):
        self.__danio = dan
    
    def get(self):
        return self.__danio
class Escudo:
    def __init__(self, defen):
        self.__defensa = defen
        
    def get(self):
        return self.__defensa
    

class Slot(Generic[T]):
    def __init__(self, item:T=None):
        self.__item:T = item
        
    def  equipar(self, nuevoItem:T):
        if(self.__item == None):
            self.__item = nuevoItem
            
    def getValor(self):
        return self.__item.get()
    
    def desequipar(self):
        self.__item = None
        
    def getItem(self):
        return self.__item
class Personaje:
    def __init__(self, nom):
        self.__nombre = nom
        self.__item = Slot()
class Main():
    esp = Espada(100)
    esc = Escudo(200)
    opt = 1
    slot = Slot[T]()
    #print(type(slot.getItem())) #imprime que tipo de dato es
    while(opt !=0):
        print("opciones: ")
        if(isinstance(slot.getItem(), Espada)):
            print("1) atacar")
        elif(isinstance(slot.getItem(), Escudo)):
            print("2) defender")
        else:
            print("4) equipar item")
        print("3)desequipar")
        print("0)salir")
        opt = int(input("escriba un numero: "))
        if(opt == 1):
            print(f"se realizo {slot.getValor()} de daño con la espada")
        elif( opt ==2):
            print(f"se defendio con -{slot.getValor()} de danio")
        elif(opt == 3):
            slot.desequipar()
        elif(opt == 4):
            
            print('''
que desea equipar:
1) espada
2) escudo''')
            o = int(input())
            if(o == 1):
                slot = Slot[Espada]()
                slot.equipar(esp)
            else:
                slot = Slot[Escudo]()
                slot.equipar(esc)