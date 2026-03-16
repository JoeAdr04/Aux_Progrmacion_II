class  PoligonoRegular:
    
    def __init__(self, n=3,lado=1,x=0,y=0):
        self.__n = n
        self.__lado = lado
        self.__x = x
        self.__y = y
        
class AlegebraVectorial:
    
    def __init__(self,a = []):
        self.a =a
    
    def getVect(self):
        return self.a
        
    def __add__(self, b:"AlegebraVectorial"):
        if(isinstance(b, AlegebraVectorial)):
            return b.getVect()

    
class Main():
    p = PoligonoRegular()
    p1 = PoligonoRegular(4,2)
    p2 = PoligonoRegular(4,2,3,2)
    print(p,p1)
    a = AlegebraVectorial()
    a2 = AlegebraVectorial([1,2,3,4])
    print(a+a2)
    
    #p+p1