class EdadInvalidaException(Exception):
    def __init__(self, *args):
        super().__init__("edad incorrecta")
        
class SaldoInsuficienteException(Exception):
    def __init__(self, saldo =None, retiro = None):
        self.__saldo = saldo
        self.__retiro = retiro
        m = f"saldo inscuficiente por que {self.__retiro} es mayor que {self.__saldo}"
        super().__init__(m)
        
    

class Main():
    '''edad = int(input("ingresa tu edad"))
    try:
        #hace mas cosas
        if edad < 0:
            raise EdadInvalidaException()
    except EdadInvalidaException:
        print("ingresaste un numero negativo")'''
    
    try:
        sal = int(input("ingresa tu saldo: "))
        ret = int(input("cuanto vas a retirar: "))
        if (ret > sal):
            raise SaldoInsuficienteException(sal, ret)
        
    except SaldoInsuficienteException as e:
        print(f"se retirara todo el saldo {e}")
    finally:
        sal = 0
        print(f"Nuevo saldo: {sal}")
        
    try:
        arch = open("datos.txt")
    except FileNotFoundError:
        print("archivo inexistente")
