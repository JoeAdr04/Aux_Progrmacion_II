from multimethod import multimethod
class Calculadora:
    @multimethod
    def suma(self, a:int,b:int, c:int):
        return a+b+c
    @multimethod
    def suma(self, a:int,b:int):
        return a+b
    
    @multimethod
    def multiplicar(self, a:int,b:int):
        return a*b
    
    @multimethod
    def multiplicar(self, a:float,b:float):
        return a*b
    
    '''agregar una funcion que reciba mi nombre y mi apellido
    ademas de un numero, si es flotante solo muestra mi 
    apellido si es entero me saluda esa cantidad 
    de veces
    '''

class Main():
    c = Calculadora()
    print(c.suma(4,5))
    print(c.suma(4,5,6))