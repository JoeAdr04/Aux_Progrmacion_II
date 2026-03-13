from multimethod import multimethod

class Celular:
    def __init__(self, num=0, marc=""):
        self.__numero = num
        self.__marca = marc
        
    def __str__(self):
        return f"numero: {self.__numero}, marcha:{self.__marca}"

    @multimethod
    def llamar(self, d:str):
        print(f"Lamando al dueño: {d}")
        
    @multimethod
    def llamar(self, d:int):
        print(f"Lamando al numero: {d}")
    
    
    
        
class Main():
    #c = Celular()
    #print(c)
    c = Celular(1234,"samsung")
    c.llamar(1234)
    c.llamar("luis")