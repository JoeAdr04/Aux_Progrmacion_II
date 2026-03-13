class Animal():
    def __init__(self, nom, ed):
        self.__nombre = nom
        self.__edad = ed
        
    def mostrar(self):
        print(f"Animal[nombre: {self.__nombre}, edad: {self.__edad}]")        
        
    def __str__(self):
        return (f"Animal[nombre: {self.__nombre}, edad: {self.__edad}]")
    def crecer(self):
        self.__edad = self.__edad+1
        print("El animal ha cumplido un año mas")
        print(f"Edad del animal: {self.__edad}")
        
    def masViejo(self, otro:"Animal"):
        if(self.__edad>otro.__edad):
            print(f"el mas viejo es:{self.__str__}")
        elif(self.__edad == otro.__edad):
            print("ambos son igual de viejos")
        else:
            print(f"el mas viejo es:{otro.__str__}")
class Main():
    a = Animal("Firulais", 4) #creacion del objeto
    print(a) #muestra al objeto
    a.crecer() #llamad a ala funcion crecer()
    
    a1 = Animal("michi", 5)
    a2 = Animal("goose", 7)
    a1.masViejo(a2)