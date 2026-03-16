from multimethod import multimethod
class Producto:
    def __init__(self, nom="", pre=0.0, cod = 0):
        self.nombre = nom
        self.precio = pre
        self.codigo = cod
    
    def __str__(self):
        return f"nombre:{self.nombre}, precio:{self.precio}, codigo:{self.codigo}"
    
    @multimethod
    def cacularTotal(self,x:str):
        return self.precio
    
    @multimethod
    def cacularTotal(self, des:float):
        return self.precio-(self.precio*des)
    
    @multimethod
    def mostrar(self, x:bool):
        print(self)
    @multimethod    
    def mostrar(self, desc:float):
        total =self.cacularTotal(desc)
        print(f"nombre:{self.nombre}, total:{total}")
        
    @multimethod
    def modPrecio(self, x:int):
        self.precio = self.precio*1.20
        
    @multimethod
    def modPrecio(self, x:float):
        self.precio = x
        
class Perro:
    def __str__(self):
        pass
    
    
class Main():
    p = Perro()
    print(p)
    p1 = Producto("leche", 12.5, 123123)
    p2 = Producto("carne", 12.5)
    p3 = Producto("dinosaurio")
    
    #print(p1.cacularTotal("hola"))
    #print(p1.cacularTotal(0.15))
    p1.mostrar(True)
    p1.mostrar(0.15)
    
    p1.modPrecio(2)
    print(p1)
    p2.modPrecio(141.5)
    print(p2)