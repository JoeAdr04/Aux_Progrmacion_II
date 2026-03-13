from multimethod import multimethod
class Calculadora:
    @multimethod
    def suma(self, a:int,b:int, c:int):
        return a+b+c
    @multimethod
    def suma(self, a:int,b:int):
        return a+b
    
class Main():
    c = Calculadora()
    print(c.suma(4,5))
    print(c.suma(4,5,6))