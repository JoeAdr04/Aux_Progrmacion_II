'''
Realiza la abstracción para la clase Auto, para realizar los siguientes incisos
a) Sobrecargar el constructor 2 veces (x)
b) Instanciar 2 objetos Auto, usando los diferentes constructores. (x)
c) Sobrecargar el operador ++ para incrementar la gasolina en 5 litros. (x)
d) Sobrecargar el operador + para cambiar el color del auto. (x)
e) Sobrecargar el operador – para sumar el total de gasolina entre los 2 autos. (x)

'''
class Auto:
    def __init__(self, gasolina=0, color="blanco", capacidad = 4, placa="0000abc"):
        self.__gasolina = gasolina
        self.__color = color
        self.__capacidad = capacidad
        self.__placa = placa
        
    def aumentar(self):
        self.__gasolina = self.__gasolina+5
        
    def __add__(self, other):
        if(isinstance(other,str)):
            self.__color = other
        else:
            print("el color es una cadena")
            
    def __sub__(self, other):
        if(isinstance(other,Auto)):
            sum = self.__gasolina+other.__gasolina
            return Auto(sum,"rojo",4,"4321dot")
        else:
            print("debes de sumar otra instancias de auto")
        
    def __str__(self):
        return f"gasolina:{self.__gasolina}, color:{self.__color}, capacidad:{self.__capacidad}, placa:{self.__placa}"
class Main():
    a1 = Auto()
    a2 = Auto(14,"verde",6,"1234lol")
    #print(f"Auto 1:{a1}")
    #print(f"Auto 2:{a2}")
    a1.aumentar()
    a2+"negro"
    aux = a1-a2
    print(f"Auto 1:{a1}")
    print(f"Auto 2:{a2}")
    print(f"Auto 2:{aux}")