from typing import Generic, TypeVar

''' Caso java
public class Veterinaria<K,V>{
    private ArrayList<T> mascotas = new ArrayList();
    
    public Veterinaria(){
        
    }
    
    public void addElemento(T algo){
        this.mascotas.add(algo);
    }
}

class Main{
    Veterinaria<Mascota> vet = new Veterianria<>();
    Veterinaria<Aves> vet2 = new Veterianria<>();
    Mascota m = new Mascota("asdf", 12);
    Ave a = new Ave("asdf");
    vet.addElemento(m);
    vet2.addElemento(a);
}
'''

T = TypeVar('T')

class Mascota:
    def __init__(self,nom:str, ed:int):
        self.__nombre = nom
        self.__edad = ed
        
class Ave:
    def __init__(self, nom):
        self.__nombre = nom

class Veterinaria(Generic[T]): #public class Veterinaria<K,V>
    def __init__(self):
        self.__mascotas:list[T] = [] #private ArrayList<T> mascotas = new ArrayList();
        
    def addElemento(self, algo:T):
        self.__mascotas.append(algo)
        
    def mostrar(self):
        for e in self.__mascotas:
            print(e)
            
    def verifica(self):
        for e in self.__mascotas:
            if(isinstance(e, Ave)):
                print("ave detectada")
            else:
                print("mascota detectada")
                
class Main():
    v = Veterinaria[Mascota]()
    v2 = Veterinaria[Ave]()
    m = Mascota("firulais", 12)
    a = Ave("poly")
    v.addElemento(a)
    v.addElemento(m)
    v.addElemento(2)
    v.mostrar()
    v.verifica()